from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse 
from utils.logging_file import logger

# Create FastAPI app instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
async def index():
    logger.info("GET request to project root")
    return FileResponse('./pages/index.html')
      
@app.get("/home") 
async def home_page(): 
    logger.info("Request to home page")
    return FileResponse('./pages/homepage.html')  