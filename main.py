from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    # return 'hi'
    return {'data':{"name":'sabeel','age':22}}

@app.get('/about')
def about():
    return {'data':'about page'}
