## How It Works (The Logic)
User Asks a Question: The frontend sends the user's query to the Python (Flask) backend.

Vector Search (The "Brain"):

The system converts the question into numbers (embeddings) using SentenceTransformers.

It searches the FAISS Index to find the most similar question in your local database.

Hybrid Decision Engine:

High Confidence Match (>50%): If a local answer exists, it returns it immediately (Fast & Accurate).

Low Confidence Match (<50%): If the answer isn't in your database, it securely calls Google Gemini AI to generate a helpful response (General Intelligence).

Secure Response: The final answer is sent back to the frontend as JSON. 

-----------------------------------------------------------------------------------------

## 🛠️ Development Steps (What You Built)
Copy and paste this into your README under a "How it was Built" section.

## 1. Data Pipeline Setup

Created a JSON dataset (faq_data.json) containing specific banking questions and answers.

Built a Python script (build_faiss.py) to convert this text data into vector embeddings.

Implemented FAISS (Facebook AI Similarity Search) for high-speed, efficient data retrieval.

## 2. Backend API Development

Developed a Flask API (app.py) to handle incoming HTTP requests from the frontend.

Integrated SentenceTransformers (all-MiniLM-L6-v2) to understand the semantic meaning of user queries, not just keyword matching.

## 3. Hybrid AI Integration

Implemented a "Hybrid Logic" system in Python.

Integrated Google Gemini API as a fallback intelligence layer for general banking queries.

Added error handling to ensure the bot always replies, even if the AI service is down.

## 4. Security & Optimization

Secured sensitive API keys using Environment Variables (.env) to prevent leaks.

Optimized the model selection (switching to gemini-flash-latest) for faster response times.

Configured CORS to allow secure communication between the chat interface and the backend server.
