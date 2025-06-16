# 🚀 Smart Assistant - Quick Start Guide

## 📋 Prerequisites
- **Python 3.8+** must be installed on your system
- Download from: https://www.python.org/downloads/
- Ensure you check the "Add to PATH" option for fresh installation.

## ⚡ Get Started in 4 Steps

### 1. **Setup Environment** (Required - First Time Only)
Run: `setup_environment.bat`
*Note: Virtual environment files are excluded from git, so this step is always required for new installations.*

### 2. **Setup API Keys** (Required)
Edit `.env` file (rename `secrets.env` to `.env`) and add your API keys:
```properties
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  
ANTHROPIC_API_KEY=your_claude_api_key_here
```

**Get API Keys:**
- **Gemini (Free)**: https://aistudio.google.com/app/apikey
- **OpenAI**: https://platform.openai.com/api-keys  
- **Claude**: https://console.anthropic.com/


### 3. **Start the Server**
Double-click: `start_server.bat`

Or run in PowerShell: `.\start_server.ps1`


### 4. **Open Web Interface**
Browser opens automatically to: http://localhost:8000


### 5. **Connect ArcGIS Pro** (Optional)
Open ArcGIS Pro, locate `SmartAssistant.atbx` in the Catalog pane, and run the script tool inside it.


---

### **Manual Server Start**
```batch
call activate_environment.bat
python run.py
```

### **Available AI Models**
- ✅ **Gemini Flash** (Recommended - Fast & Free)
- ✅ **Gemini Pro** (Advanced reasoning)  
- ✅ **GPT-4 Turbo** (OpenAI premium)
- ✅ **GPT-4o** (Latest OpenAI model)
- ✅ **Claude Sonnet** (Anthropic)

---

## ❓ Troubleshooting

**Server won't start?**
→ Run `setup_environment.bat`

**API errors?**  
→ Check your API keys in `.env`

**ArcGIS connection fails?**
→ Verify paths in `connect_arcgis.bat`

**Python not found?**
→ Install Python 3.8+ and ensure it's in your PATH

---

## ✅ What's Working
- 🤖 Multi-AI Model Support (OpenAI, Gemini, Claude)
- 💬 Real-time Chat Interface
- 🗺️ 27 GIS Analysis Functions  
- 🧠 Conversation Memory
- 🌍 Arabic & English Language Support
- 📦 Self-contained Environment (Portable)

**Status: Production Ready** 🎉

