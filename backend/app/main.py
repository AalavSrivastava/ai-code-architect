from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def root():
return {"status":"ok"}
@app.get('/movies')
def list_movies():
sample = [{"id":1,"title":"The Matrix"},{"id":2,"title":"Inception"}]
return sample
@app.get('/recommend')
def recommend(user_id: int = 1):
# Dummy recommender
return [{"id":2,"title":"Inception"}]
