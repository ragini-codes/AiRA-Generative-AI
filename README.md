# AiRA - AI Chatbot

AiRA is a generative AI chatbot built using Python, Flask, and Google's Gemini API. It provides an interactive conversational experience through a web interface.

## Features

- AI-powered conversational responses
- Web interface built with HTML
- Backend powered by Flask
- Integration with Google's Gemini API

## Technologies Used

- Python
- Flask
- HTML
- Google Gemini API
- python-dotenv

## Project Structure

```text
aira-ai-chatbot/
├── airacode.py
├── requirements.txt
├── .gitignore
└── templates/
    └── index.html
```

## Setup and Installation

1. Clone this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Gemini API key:

   ```text
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the application:

   ```bash
   python airacode.py
   ```

5. Open the local URL displayed in your terminal in your browser.

## Security

Keep your API key private. Never upload your `.env` file or expose your API key in the source code.

## Note

This project was developed collaboratively as a group project.
