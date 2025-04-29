from fastapi import FastAPI

app: FastAPI = FastAPI()

#App routes
@app.get('/')
def home():
    return {
        'message': 'Calculator app running!'
    }

@app.get('/add')
def add(x: float, y: float):
    return {
        'result': x + y
    }

@app.get('/subtract')
def subtract(x: float, y: float):
    return {
        'result': x - y
    }

@app.get('/multiply')
def multiply(x: float, y: float):
    return {
        'result': x * y
    }

@app.get('/divide')
def divide(x: float, y: float):
    if y == 0:
        return {
            'result': 'Error: Division by zero not feasible'
        }
    return {
        'result': x / y
    }
