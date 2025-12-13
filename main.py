from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string

app = FastAPI()

# This is our in-memory database
# Structure: {'abc12': 'https://google.com'}
url_database = {}

def generate_short_code():
    """Helper function to generate a random 5-character string"""
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    return ''.join(random.choice(characters) for _ in range(5))

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Shortener API"}

@app.post("/shorten")
def shorten_url(long_url: str):
    # 1. Generate a random code
    short_code = generate_short_code()
    
    # 2. Save it to our database
    url_database[short_code] = long_url
    
    # 3. Return the result
    return {
        "message": "URL Shortened successfully", 
        "short_code": short_code,
        "original_url": long_url
    }

@app.get("/{short_code}")
    # 1. Look up the code in the database
def redirect_to_url(short_code: str):
    if short_code in url_database:
        target_url = url_database[short_code]

        return RedirectResponse(url = target_url)
    else:
        # Return a 404 Error if not found
        raise HTTPException(status_code=404, detail="URL not found")