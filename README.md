# ai-code-architect
A multi-agent AI system that converts plain-English ideas into complete full-stack project scaffolds (React + FastAPI). Built for the Kaggle × Google AI Intensive 2025 Capstone, demonstrating tools, memory, multi-agent workflows, long-running tasks, and A2A protocol

# AI Code Architect & Project Builder
This repository contains a demo implementation of a multi-agent system that 
generates a full-stack project (React + FastAPI) from a plain-English idea.
## Features
- Multi-agent workflow (Requirements → Architecture → CodeGen → Reviewer)
- Tools: File writer, JSON validator, linter stub, code exec stub
- Memory: simple MemoryBank to persist preferences
- Long-running generation simulated with sleeps and chunked writes
- Observability via logging
## How to run
1. `python main.py "Build a todo app with FastAPI and React"`
2. Inspect `generated_project/` for created files.
## Notes
Replace stubbed tools with ADK tool wrappers and configure Gemini in a 
production version. Do NOT add API keys to the repo.
