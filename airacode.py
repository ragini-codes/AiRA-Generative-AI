# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 22:49:23 2026

@author: pappu
"""

from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

print("Current folder:", os.getcwd())
print("Python file:", os.path.abspath(__file__))

print("Templates folder exists:", os.path.isdir("templates"))
print("HTML file exists:", os.path.isfile("templates/index.html"))
print("Files in current folder:", os.listdir())

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Flask app setup
app = Flask(__name__)

def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-3.8-flash")
        response = model.generate_content(user_input)
        text_response = response._result.candidates[0].content.parts[0].text

        # Check if the response contains bullet points and reformat them
        # Convert separate bullet points into a cohesive message
        if "•" in text_response:  # Check if the text contains bullets
            text_response = text_response.replace("•", "\n•")  # Make sure the bullets stay together in one message
        return text_response
    except Exception as e:
        print("Error communicating with Gemini:", e)
        return "I am having trouble responding at the moment."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400
    
    # Get response from Gemini
    gemini_response = get_gemini_response(user_input)
    
    return jsonify({
        "gemini_response": gemini_response
    })

if __name__ == "__main__":
    app.run(debug=False)
