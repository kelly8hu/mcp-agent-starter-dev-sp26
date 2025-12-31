# MCP Agent Mini-Project (OpenAI Agents SDK)

This project is a starter template for building a small AI agent that can use real tools exposed via a local MCP server.

## What you’re building
A CLI agent that can:
- respond normally to user prompts
- call MCP tools when helpful (e.g., generate a brief, save text, make a checklist)

The agent loop is handled by the OpenAI Agents SDK (`Runner.run`), which repeatedly calls the model and executes tool calls until a final output is produced. 

## Setup

### 1) Clone your repo and open in VS Code
```bash
git clone <YOUR_REPO_URL>
cd <YOUR_REPO_FOLDER>
code .
```

### 2) Create and activate a virtual environment

Python: 
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows (Powershell):

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

```bash
pip install -r requirements.txt

```

### 4) Add your API key 

Log into your OpenAI account to get your secret unique API key. Add this to the .env file

### 5) Run 

```bash
python agent_app.py 
```

