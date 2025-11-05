# Module 1: Setup

## Notes
- See fastapi's [`pyproject.toml`](https://github.com/fastapi/fastapi/blob/master/pyproject.toml) for fast api dependencies 

## Steps

### Setup Project

<details><summary>1. Create virtual environment:</summary>
  
- `python -m venv .venv`
</details>

<details><summary>2. Activate environment (windows):</summary>
  
- `.\.venv\Scripts\Activate.ps1`
</details>


<details><summary>3. Install fastAPI:</summary>
  
- `pip install fastapi`
- `pip install fastapi-cli`
</details>

<details><summary>4. Extract installed packages to requirements.txt:</summary>
  
- `pip freeze > requirements.txt`
</details>

--

### Create dummy endpoint

<details><summary>1. Create project folder</summary>
  
- Create `app` directory (can also call it `main`, `src`, etc)
- Create `main.py` inside app directory
</details>

<details><summary>2. Add the following code to `main.py`</summary>
  
  ```python
  from fastapi import FastAPI

  app = FastAPI()

  @app.get("/hello")
  async def root():
      return {"message":"Hello World"}
  ```
</details>

<details><summary>3. Run project</summary>
  
- `fastapi dev .\app\main.py`
</details>

<details><summary>4. Test endpoint</summary>
  
- Open up browser
- Go to `http://127.0.0.1:8000/docs`
- Go to `http://127.0.0.1:8000/hello`
</details>
