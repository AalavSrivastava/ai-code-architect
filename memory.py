# memory.py
# Very small memory bank to demonstrate sessions & long-term memory.

class InMemorySessionService:
def __init__(self):
self.sessions = {}
def create_session(self, session_id):
self.sessions[session_id] = {}
return self.sessions[session_id]
def get_session(self, session_id):
return self.sessions.get(session_id, None)
class MemoryBank:
def __init__(self):
self.store_dict = {}
def store(self, key, value):
self.store_dict[key] = value
def recall(self, key):
return self.store_dict.get(key)
