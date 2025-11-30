# tools.py
# Simple tool implementations that can be replaced by ADK Tool wrappers.
import json
import os
class FileWriterTool:
def write(self, path, content):
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
f.write(content)
return True
class JSONValidatorTool:
def validate(self, obj):
try:
json.dumps(obj)
return True, None
except Exception as e:
return False, str(e)
class CodeExecTool:
def run(self, filepath):
# Warning: running arbitrary code is unsafe. This is a stub for unit 
tests only.
return True, "exec stub"
class LintTool:
def lint(self, filepath):
# Very basic: check the file exists and is non-empty
try:
with open(filepath, 'r', encoding='utf-8') as f:
data = f.read().strip()
if len(data) == 0:
return False, "Empty file"
return True, "OK"
except FileNotFoundError:
return False, "File not found"
