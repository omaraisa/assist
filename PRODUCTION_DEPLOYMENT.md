# 🚀 Production Deployment Guide

## 📋 Overview
This guide covers deploying the ArcGIS Pro Smart Assistant FastAPI application in production environments.

## 🐳 Docker Deployment

### Prerequisites
- Docker and Docker Compose installed
- Environment variables configured
- SSL certificates (for HTTPS)

### Quick Deploy
```bash
# Clone and navigate to project
cd SmartAssistantFastAPI

# Copy environment template
cp .env.template .env.production

# Edit production environment variables
# Set your API keys and production settings

# Build and start containers
docker-compose up -d

# Check health
curl http://localhost:8000/health
```

### Environment Configuration
```env
# .env.production
GEMINI_API_KEY=your_production_gemini_key
OPENAI_API_KEY=your_production_openai_key
ANTHROPIC_API_KEY=your_production_claude_key

# Production settings
DEBUG=false
HOST=0.0.0.0
PORT=8000
LOG_LEVEL=INFO

# Security
CORS_ORIGINS=["https://yourdomain.com"]
ALLOWED_HOSTS=["yourdomain.com"]

# Performance
WS_MAX_CONNECTIONS=1000
REQUEST_TIMEOUT=300
```

## ☁️ Cloud Deployment

### AWS Deployment (ECS/Fargate)
```yaml
# ecs-task-definition.json
{
    "family": "smart-assistant",
    "networkMode": "awsvpc",
    "requiresCompatibilities": ["FARGATE"],
    "cpu": "1024",
    "memory": "2048",
    "containerDefinitions": [
        {
            "name": "smart-assistant",
            "image": "your-registry/smart-assistant:latest",
            "portMappings": [
                {
                    "containerPort": 8000,
                    "protocol": "tcp"
                }
            ],
            "environment": [
                {"name": "GEMINI_API_KEY", "value": "your-key"},
                {"name": "DEBUG", "value": "false"}
            ],
            "logConfiguration": {
                "logDriver": "awslogs",
                "options": {
                    "awslogs-group": "/ecs/smart-assistant",
                    "awslogs-region": "us-east-1",
                    "awslogs-stream-prefix": "ecs"
                }
            }
        }
    ]
}
```

### Azure Container Instances
```yaml
# azure-container-instance.yml
apiVersion: 2018-10-01
location: eastus
name: smart-assistant
properties:
  containers:
  - name: smart-assistant
    properties:
      image: your-registry/smart-assistant:latest
      resources:
        requests:
          cpu: 1
          memoryInGb: 2
      ports:
      - port: 8000
      environmentVariables:
      - name: GEMINI_API_KEY
        value: your-key
      - name: DEBUG
        value: 'false'
  osType: Linux
  ipAddress:
    type: Public
    ports:
    - protocol: tcp
      port: 8000
```

### Google Cloud Run
```yaml
# cloudbuild.yaml
steps:
- name: 'gcr.io/cloud-builders/docker'
  args: ['build', '-t', 'gcr.io/$PROJECT_ID/smart-assistant', '.']
- name: 'gcr.io/cloud-builders/docker'
  args: ['push', 'gcr.io/$PROJECT_ID/smart-assistant']
- name: 'gcr.io/cloud-builders/gcloud'
  args:
  - 'run'
  - 'deploy'
  - 'smart-assistant'
  - '--image'
  - 'gcr.io/$PROJECT_ID/smart-assistant'
  - '--platform'
  - 'managed'
  - '--region'
  - 'us-central1'
  - '--allow-unauthenticated'
  - '--set-env-vars'
  - 'GEMINI_API_KEY=your-key,DEBUG=false'
```

## 🔒 Security Considerations

### SSL/TLS Configuration
```nginx
# nginx.conf
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    ssl_certificate /etc/ssl/certs/yourdomain.com.crt;
    ssl_certificate_key /etc/ssl/private/yourdomain.com.key;
    
    location / {
        proxy_pass http://smart-assistant:8000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### API Key Management
- Use environment variables or secret management services
- Rotate API keys regularly
- Monitor API usage and set quotas
- Implement rate limiting

### Network Security
- Use VPC/private networks
- Configure firewalls and security groups
- Enable DDoS protection
- Use Web Application Firewall (WAF)

## 📊 Monitoring and Logging

### Health Checks
- `/health` - Basic health status
- `/metrics` - Performance metrics
- `/stats` - Usage statistics

### Logging Configuration
```python
# Production logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/app/logs/production.log',
            'maxBytes': 10485760,  # 10MB
            'backupCount': 5,
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',
    },
}
```

### Monitoring Integration
```python
# Prometheus metrics (optional)
from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter('requests_total', 'Total requests')
REQUEST_LATENCY = Histogram('request_duration_seconds', 'Request latency')
ACTIVE_CONNECTIONS = Gauge('active_connections', 'Active WebSocket connections')
```

## 🔧 Performance Optimization

### Resource Limits
```yaml
# docker-compose.override.yml
version: '3.8'
services:
  smart-assistant:
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
        reservations:
          cpus: '1'
          memory: 2G
```

### Caching Strategy
- Redis for session storage
- CDN for static assets
- API response caching

### Load Balancing
```yaml
# Load balancer configuration
version: '3.8'
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx-lb.conf:/etc/nginx/nginx.conf
  
  smart-assistant-1:
    build: .
    environment:
      - INSTANCE_ID=1
  
  smart-assistant-2:
    build: .
    environment:
      - INSTANCE_ID=2
```

## 🚨 Backup and Recovery

### Database Backup
```bash
# Backup conversation history (if using database)
docker exec smart-assistant pg_dump -U postgres smart_assistant > backup.sql
```

### Configuration Backup
```bash
# Backup configuration files
tar czf config-backup.tar.gz .env nginx.conf docker-compose.yml
```

### Disaster Recovery Plan
1. **Automated backups** - Daily configuration and data backups
2. **Infrastructure as Code** - Version control all deployment configs
3. **Multi-region deployment** - Deploy in multiple availability zones
4. **Monitoring alerts** - Set up alerts for system failures

## 📈 Scaling Strategies

### Horizontal Scaling
- Deploy multiple instances behind load balancer
- Use Redis for shared session storage
- Implement sticky sessions for WebSocket connections

### Vertical Scaling
- Increase container resources (CPU/memory)
- Optimize Python performance (uvloop, etc.)
- Database optimization

### Auto-scaling
```yaml
# Kubernetes HPA example
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: smart-assistant-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: smart-assistant
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

## 🔍 Troubleshooting

### Common Issues
1. **High memory usage** - Check conversation history limits
2. **WebSocket disconnections** - Verify load balancer configuration
3. **API rate limits** - Monitor and adjust API usage
4. **SSL certificate issues** - Verify certificate validity and paths

### Debug Commands
```bash
# Check container logs
docker logs smart-assistant

# Monitor resource usage
docker stats smart-assistant

# Test health endpoints
curl -f http://localhost:8000/health
curl -f http://localhost:8000/metrics

# WebSocket connection test
wscat -c ws://localhost:8000/ws
```

---

## ✅ Production Checklist

- [ ] Environment variables configured
- [ ] SSL/TLS certificates installed
- [ ] Database backups configured
- [ ] Monitoring and alerting set up
- [ ] Load testing completed
- [ ] Security audit performed
- [ ] Documentation updated
- [ ] Team training completed

---

**🎉 Your ArcGIS Pro Smart Assistant is now production-ready!**
