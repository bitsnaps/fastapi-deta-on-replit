# pip install fastapi
# pip install uvicorn
# Run the app:
# uvicorn main:app --reload
# then try to access http://localhost:8000/
# and http://localhost:8000/docs for documentation 
import os
from fastapi import FastAPI
from deta import Deta

#To get your deta project key, you can store it replit's secrets tool, then invoke it with:
#os.getenv("DETA_PROJECT_KEY")

# This how to connect to or create a database (the DATASETS_KEY is the name of Collection in deta space here)
datasets_key = os.environ['DATASETS_KEY']
deta = Deta(datasets_key)
db = deta.Base("users")
#drive = deta.Drive("main_drive")

app = FastAPI()

@app.get('/')
def index():
  return {'api':"go to /docs"}

@app.get('/users/{key}')
def get_user_by_key(key: str):
  user = db.get(key)
  return {'users': [user]}

@app.get('/users')
def get_all_users():
  users = db.fetch()
  return {'users':users}

#@app.post('/users')
#def create_user(user_name: str):
#  user = db.put({"name": user_name}) # key will be auto-generated
#  return {'user': user }