# Module 1: Setup

## Notes
- See fastapi's [`pyproject.toml`](https://github.com/fastapi/fastapi/blob/master/pyproject.toml) for fast api dependencies 

## Steps

**Setup Project**

Create virtual environment: 
- `python -m venv .venv`

Activate environment (windows): 
- `.\.venv\Scripts\Activate.ps1`

Install fastAPI: 
- `pip install fastapi`
- `pip install fastapi-cli[stand`

Extract installed packages to requirements.txt: 
- `pip freeze > requirements.txt`

**Create dummy endpoint**
Create project folder
- Create `app` directory (can also call it `main`, `src`, etc)
- Create `main.py` inside app directory

Add the following code to `main.py`
  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/hello")
  async def root():
      return {"message":"Hello World"}
  ```

Run project
- `fastapi dev .\app\main.py`

Test endpoint
- Open up browser
- Go to `http://127.0.0.1:8000/docs`
- Go to `http://127.0.0.1:8000/hello`