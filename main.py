from fastapi import FastAPI # Import a web framework that's used to build APIs
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone 

app = FastAPI() # Create an instance of the FastAPI class

# Add CORS middleware to handle Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow all domains (adjust for production)
    allow_credentials=True,       # Enable cookies/authorization headers
    allow_methods=["GET"],          # Allow all HTTP methods
    allow_headers=["*"],          # Allow all HTTP headers
)

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

