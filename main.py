# main.py
# Demo entrypoint that wires tools, memory, agents and runs a sample idea.
import sys
from agents import RequirementsAgent, ArchitectureAgent, CodeGeneratorAgent,
ReviewerAgent, SequentialSystem
from tools import FileWriterTool, JSONValidatorTool, CodeExecTool, LintTool
from memory import MemoryBank, InMemorySessionService
def build_system():
memory = MemoryBank()
session = InMemorySessionService()
file_tool = FileWriterTool()
json_validator = JSONValidatorTool()
code_exec = CodeExecTool()
linter = LintTool()
req = RequirementsAgent("requirements", tools=[json_validator],
memory=memory)
arch = ArchitectureAgent("architecture", tools=[json_validator],

memory=memory)
gen = CodeGeneratorAgent("codegen", tools=[file_tool, code_exec],
memory=memory)
rev = ReviewerAgent("reviewer", tools=[linter], memory=memory)
system = SequentialSystem([req, arch, gen, rev])
return system
if __name__ == '__main__':
idea = "Build a movie recommendation app with FastAPI backend and React 
frontend"
if len(sys.argv) > 1:
idea = sys.argv[1]
system = build_system()
result = system.run(idea)
print("---SUMMARY---")
print(result)
print("Generated project is under generated_project/")
