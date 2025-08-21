"""
Monitoring and analytics service for Progent
"""

import time
import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from collections import defaultdict, deque
from dataclasses import dataclass, asdict
import logging

logger = logging.getLogger(__name__)

@dataclass
class ConnectionMetrics:
    """Metrics for WebSocket connections"""
    total_connections: int = 0
    active_connections: int = 0
    arcgis_connections: int = 0
    web_connections: int = 0
    failed_connections: int = 0
    avg_connection_duration: float = 0.0

@dataclass
class AIMetrics:
    """Metrics for AI service usage"""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    avg_response_time: float = 0.0
    model_usage: Dict[str, int] = None
    
    def __post_init__(self):
        if self.model_usage is None:
            self.model_usage = {}

@dataclass
class FunctionMetrics:
    """Metrics for spatial function calls"""
    total_calls: int = 0
    successful_calls: int = 0
    failed_calls: int = 0
    avg_execution_time: float = 0.0
    function_usage: Dict[str, int] = None
    
    def __post_init__(self):
        if self.function_usage is None:
            self.function_usage = {}

class MonitoringService:
    """Service for monitoring system metrics and performance"""
    
    def __init__(self, retention_hours: int = 24):
        self.retention_hours = retention_hours
        self.start_time = datetime.now()
        
        # Metrics storage
        self.connection_metrics = ConnectionMetrics()
        self.ai_metrics = AIMetrics()
        self.function_metrics = FunctionMetrics()
        
        # Time series data (last 24 hours by default)
        self.connection_history = deque(maxlen=retention_hours * 60)  # Per minute
        self.response_times = deque(maxlen=1000)  # Last 1000 requests
        self.error_logs = deque(maxlen=500)  # Last 500 errors
        
        # Active connections tracking
        self.active_connections = {}
        self.connection_start_times = {}
        
        logger.info("Monitoring service initialized")
    
    # Connection Monitoring
    def track_connection_start(self, client_id: str, client_type: str):
        """Track new connection"""
        self.active_connections[client_id] = {
            "type": client_type,
            "start_time": datetime.now(),
            "messages_sent": 0,
            "messages_received": 0
        }
        
        self.connection_metrics.total_connections += 1
        self.connection_metrics.active_connections += 1
        
        if client_type == "arcgis_pro":
            self.connection_metrics.arcgis_connections += 1
        elif client_type == "chatbot":
            self.connection_metrics.web_connections += 1
        
        logger.info(f"Connection tracked: {client_id} ({client_type})")
    
    def track_connection_end(self, client_id: str):
        """Track connection end"""
        if client_id in self.active_connections:
            connection_info = self.active_connections[client_id]
            duration = (datetime.now() - connection_info["start_time"]).total_seconds()
            
            # Update average connection duration
            current_avg = self.connection_metrics.avg_connection_duration
            total_connections = self.connection_metrics.total_connections
            self.connection_metrics.avg_connection_duration = (
                (current_avg * (total_connections - 1) + duration) / total_connections
            )
            
            del self.active_connections[client_id]
            self.connection_metrics.active_connections -= 1
            
            logger.info(f"Connection ended: {client_id}, duration: {duration:.2f}s")
    
    def track_connection_error(self, client_id: str, error: str):
        """Track connection error"""
        self.connection_metrics.failed_connections += 1
        self.error_logs.append({
            "timestamp": datetime.now().isoformat(),
            "type": "connection_error",
            "client_id": client_id,
            "error": error
        })
    
    # AI Service Monitoring
    def track_ai_request_start(self, request_id: str, model: str):
        """Track AI request start"""
        self.connection_start_times[request_id] = {
            "start_time": time.time(),
            "model": model
        }
    
    def track_ai_request_end(self, request_id: str, success: bool):
        """Track AI request completion"""
        if request_id in self.connection_start_times:
            request_info = self.connection_start_times[request_id]
            response_time = time.time() - request_info["start_time"]
            model = request_info["model"]
            
            # Update metrics
            self.ai_metrics.total_requests += 1
            if success:
                self.ai_metrics.successful_requests += 1
            else:
                self.ai_metrics.failed_requests += 1
            
            # Update response time
            self.response_times.append(response_time)
            if self.response_times:
                self.ai_metrics.avg_response_time = sum(self.response_times) / len(self.response_times)
            
            # Update model usage
            if model not in self.ai_metrics.model_usage:
                self.ai_metrics.model_usage[model] = 0
            self.ai_metrics.model_usage[model] += 1
            
            del self.connection_start_times[request_id]
            
            logger.info(f"AI request completed: {request_id}, model: {model}, time: {response_time:.2f}s, success: {success}")
    
    # Function Call Monitoring
    def track_function_call_start(self, call_id: str, function_name: str):
        """Track spatial function call start"""
        self.connection_start_times[call_id] = {
            "start_time": time.time(),
            "function": function_name
        }
    
    def track_function_call_end(self, call_id: str, success: bool):
        """Track spatial function call completion"""
        if call_id in self.connection_start_times:
            call_info = self.connection_start_times[call_id]
            execution_time = time.time() - call_info["start_time"]
            function_name = call_info["function"]
            
            # Update metrics
            self.function_metrics.total_calls += 1
            if success:
                self.function_metrics.successful_calls += 1
            else:
                self.function_metrics.failed_calls += 1
            
            # Update execution time
            current_avg = self.function_metrics.avg_execution_time
            total_calls = self.function_metrics.total_calls
            self.function_metrics.avg_execution_time = (
                (current_avg * (total_calls - 1) + execution_time) / total_calls
            )
            
            # Update function usage
            if function_name not in self.function_metrics.function_usage:
                self.function_metrics.function_usage[function_name] = 0
            self.function_metrics.function_usage[function_name] += 1
            
            del self.connection_start_times[call_id]
            
            logger.info(f"Function call completed: {call_id}, function: {function_name}, time: {execution_time:.2f}s, success: {success}")
    
    # Analytics and Reporting
    def get_system_health(self) -> Dict[str, Any]:
        """Get overall system health metrics"""
        uptime = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "status": "healthy" if self.connection_metrics.active_connections > 0 else "idle",
            "uptime_seconds": uptime,
            "uptime_formatted": str(timedelta(seconds=int(uptime))),
            "connections": asdict(self.connection_metrics),
            "ai_service": asdict(self.ai_metrics),
            "functions": asdict(self.function_metrics),
            "recent_errors": list(self.error_logs)[-10:],  # Last 10 errors
            "performance": {
                "avg_response_time": self.ai_metrics.avg_response_time,
                "success_rate": (
                    self.ai_metrics.successful_requests / max(self.ai_metrics.total_requests, 1) * 100
                ),
                "function_success_rate": (
                    self.function_metrics.successful_calls / max(self.function_metrics.total_calls, 1) * 100
                )
            }
        }
    
    def get_usage_statistics(self) -> Dict[str, Any]:
        """Get detailed usage statistics"""
        return {
            "ai_models": self.ai_metrics.model_usage,
            "peak_connections": max(
                [conn.get("active_connections", 0) for conn in self.connection_history] or [0]
            ),
            "total_sessions": self.connection_metrics.total_connections,
            "error_rate": (
                (self.connection_metrics.failed_connections + self.ai_metrics.failed_requests) /
                max(self.connection_metrics.total_connections + self.ai_metrics.total_requests, 1) * 100
            )
        }
    
    async def start_periodic_logging(self, interval_minutes: int = 15):
        """Start periodic logging of system metrics"""
        while True:
            try:
                health = self.get_system_health()
                logger.info(f"System Health Report: {json.dumps(health, indent=2)}")
                await asyncio.sleep(interval_minutes * 60)
            except Exception as e:
                logger.error(f"Error in periodic logging: {e}")
                await asyncio.sleep(60)  # Retry after 1 minute

# Global monitoring service instance
monitoring_service = MonitoringService()
