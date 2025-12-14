# 🔗 FastAPI URL Shortener – Detailed Documentation

## 📌 Project Overview

This project is a **simple URL Shortener backend application** built using **FastAPI**.
It converts long URLs into short, unique codes and redirects users back to the original URL when the short code is accessed.

This project is designed for:

* Backend learning
* FastAPI practice
* Interview preparation
* Git & GitHub workflow practice

---

## 🏗️ Project Structure

```
url_shortener/
│
├── main.py              # FastAPI application code
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files for Git
```

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **FastAPI** – Web framework
* **Uvicorn** – ASGI server
* **Git & GitHub** – Version control

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Varap04/url_shortener.git
cd url_shortener
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
uvicorn main:app --reload
```

Application will run at:

```
http://127.0.0.1:8000
```

Swagger UI (API testing):

```
http://127.0.0.1:8000/docs
```

---

## 🧠 How the Application Works (High Level)

1. User sends a **long URL** to the API
2. Server generates a **random 5-character short code**
3. The mapping is stored in memory (dictionary)
4. User receives the short code
5. When the short code is accessed, the user is **redirected** to the original URL

---

## 📂 Code Explanation (main.py)

### 🔹 Import Statements

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import random
import string
```

* `FastAPI` → Creates the API application
* `HTTPException` → Handles errors (404, etc.)
* `RedirectResponse` → Redirects short URL to original URL
* `random` & `string` → Generate random short codes

---

### 🔹 Create FastAPI App

```python
app = FastAPI()
```

This initializes the FastAPI application instance.

---

### 🔹 In-Memory Database

```python
url_database = {}
```

* Stores mappings of short code → original URL
* Example:

```python
{
  "A9k2P": "https://google.com"
}
```

⚠️ Data is lost when the server restarts.

---

### 🔹 Short Code Generator Function

```python
def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))
```

**Explanation:**

* Uses letters (a–z, A–Z) and digits (0–9)
* Randomly selects 5 characters
* Returns a unique short string

Example outputs:

```
A9k2P
xY8Qm
1aB9Z
```

---

### 🔹 Root Endpoint

```python
@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Shortener API"}
```

* Checks if API is running
* Returns a welcome message

---

### 🔹 Shorten URL Endpoint

```python
@app.post("/shorten")
def shorten_url(long_url: str):
```

**Flow:**

1. Accepts a long URL
2. Generates a short code
3. Stores it in the dictionary
4. Returns the result

**Example Request:**

```
POST /shorten?long_url=https://google.com
```

**Example Response:**

```json
{
  "message": "URL Shortened successfully",
  "short_code": "A9k2P",
  "original_url": "https://google.com"
}
```

---

### 🔹 Redirect Endpoint

```python
@app.get("/{short_code}")
def redirect_to_url(short_code: str):
```

**Flow:**

1. Receives short code
2. Checks if it exists
3. Redirects to original URL
4. Returns 404 if not found

**Example:**

```
GET /A9k2P
```

➡️ Redirects to `https://google.com`

---

## ❌ Error Handling

```python
raise HTTPException(status_code=404, detail="URL not found")
```

* Returns proper HTTP error
* Improves API reliability

---

## 🧪 Testing the API

Use:

* Swagger UI (`/docs`)
* Browser
* Postman
* curl

---

## ⚠️ Limitations (Current Version)

* No database (in-memory only)
* No duplicate URL handling
* No authentication
* No expiration for short URLs

---

## 🚀 Future Improvements (Planned Commits)

* Collision handling
* Database (SQLite / PostgreSQL)
* Pydantic request models
* URL validation
* Environment variables
* Docker support
* Analytics (click count)

---

## 💼 Interview Talking Points

* REST API design using FastAPI
* URL shortening logic
* HTTP redirection
* Error handling
* Git version control
* Clean project structure

---

## 👤 Author

**Varap04**
Backend Developer | FastAPI | Python

---

## ⭐ Final Note

This project is built step-by-step following **industry practices**, with clean commits and scalable design.

Feel free to fork, learn, and extend 🚀
