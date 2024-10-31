from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

# Load environment variables
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("API_KEY"))

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        # Clean up unwanted characters
        response_text = re.sub(r'[^\w\s,.!?\'"]', '', response.text)  # Keeps words, whitespace, and punctuation

    return render_template("index.html", response=response_text)

if __name__ == "__main__":
    app.run(debug=True)
