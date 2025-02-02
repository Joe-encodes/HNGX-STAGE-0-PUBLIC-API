from fastapi import FastAPI # Import a web framework that's used to build APIs
from datetime import datetime, timezone 

app = FastAPI() # Create an instance of the FastAPI class

@app.get("/") # Define a route for the root of the API
def get_info():
    return {
        "email": "joseph.adamu.it@gmail.com",  # Registered HNG email
        "current_datetime": datetime.now(timezone.utc).isoformat(), # Display current datetime in UTC
        "github_url": "https://github.com/Joe-encodes/fastapi-project"
    }

if __name__ == "__main__": # Check if the script is being run directly
    import uvicorn # Import a Python Web Server to handle requests, it communicates with the API
    uvicorn.run(app, host="0.0.0.0", port=8000)

