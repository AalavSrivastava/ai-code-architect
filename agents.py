# agents.py
# ADK-style agent orchestration (pseudo/compatible with ADK-Python interfaces)
import time
import logging
from tools import FileWriterTool, JSONValidatorTool, CodeExecTool, LintTool

from memory import MemoryBank, InMemorySessionService
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ai-architect")
class AgentMessage:
def __init__(self, sender, payload):
self.sender = sender
self.payload = payload
class BaseAgent:
def __init__(self, name, tools=None, memory=None):
self.name = name
self.tools = tools or []
self.memory = memory
def run(self, input_data):
raise NotImplementedError
class RequirementsAgent(BaseAgent):
"""Extracts user stories, constraints, tech preferences."""
def run(self, idea_text):
logger.info(f"{self.name}: parsing idea")
# Use LLM in real system. Here we simulate extraction.
extracted = {
"summary": idea_text,
"features": [
"user auth",
"movie catalog",
"recommendations endpoint",
"basic UI"
],
"preferences":
{"backend":"fastapi","frontend":"react","db":"sqlite"}
}
# Save to memory
if self.memory:
self.memory.store("last_requirements", extracted)
return AgentMessage(self.name, extracted)
class ArchitectureAgent(BaseAgent):
"""Generates architecture JSON (folders, routes, models)."""
def run(self, msg: AgentMessage):
logger.info(f"{self.name}: creating architecture from requirements")
req = msg.payload
arch = {
"folders": ["backend/app","backend/app/api","backend/app/
models","frontend/src"],

"backend":{
"framework":"fastapi",
"routes":["/auth/login","/movies","/recommend"]
},
"frontend":{
"framework":"react",
"pages":["Home","MovieList","MovieDetail"]
},
"db":"sqlite",
"env":{
"PORT":8000
}
}
# Validate
for t in self.tools:
if isinstance(t, JSONValidatorTool):
ok, err = t.validate(arch)
if not ok:
logger.warning("Architecture JSON failed validation: %s",
err)
if self.memory:
self.memory.store("last_architecture", arch)
return AgentMessage(self.name, arch)
class CodeGeneratorAgent(BaseAgent):
"""Generates code files using FileWriterTool. Supports long-running chunked 
generation."""
def run(self, msg: AgentMessage):
logger.info(f"{self.name}: generating code files")
arch = msg.payload
files_created = []
# Generate backend main
backend_main = """
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root():
 return {"status":"ok"}
"""
files_created.append(("generated_project/backend/app/main.py",
backend_main))
# Frontend App.jsx
frontend_app = """
import React from 'react'
export default function App(){
5
 return <div>Hello from generated React app</div>
}
"""
files_created.append(("generated_project/frontend/src/App.jsx",
frontend_app))
# Use file writer tool
for path, content in files_created:
for t in self.tools:
if isinstance(t, FileWriterTool):
t.write(path, content)
logger.info(f"Wrote {path}")
# Simulate long running
time.sleep(0.5)
return AgentMessage(self.name, {"files": [p for p,c in files_created]})
class ReviewerAgent(BaseAgent):
"""Runs basic lint/checks and suggests fixes."""
def run(self, msg: AgentMessage):
logger.info(f"{self.name}: reviewing generated code")
files = msg.payload.get("files", [])
report = {}
for f in files:
for t in self.tools:
if isinstance(t, LintTool):
passed, notes = t.lint(f)
report[f] = {"passed":passed, "notes":notes}
return AgentMessage(self.name, report)
# Orchestration helper
class SequentialSystem:
def __init__(self, agents):
self.agents = agents
def run(self, idea_text):
a_msg = self.agents[0].run(idea_text)
b_msg = self.agents[1].run(a_msg)
c_msg = self.agents[2].run(b_msg)
d_msg = self.agents[3].run(c_msg)
return {"requirements":a_msg.payload, "architecture":b_msg.payload,
"generation":c_msg.payload, "review":d_msg.payload}
