# AI Chatbot

A simple chatbot application using Google's Gemini 2.5 Flash Lite API.

## Features

- Interactive command-line chatbot interface
- Powered by Google Gemini 2.5 Flash Lite model
- Easy to set up and use

## Prerequisites

- Python 3.7 or higher
- Google Gemini API key

## Installation

1. Clone or navigate to the project directory:
   ```bash
   cd ChatBot_Lab2
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install google-generativeai python-dotenv openai
   or
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   Replace `your_api_key_here` with your actual Google Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

## Usage

Run the chatbot:
```bash
python ai_chatbot.py
```

Once started, the chatbot will display:
```
AI Chatbot Ready (type exit to stop)
You: 
```

Type your message and press Enter. The AI will respond with a generated message. Type `exit` to quit the application.

## Example Interaction

```
AI Chatbot Ready (type exit to stop)
You: Hello, how are you?
AI: Hello! I'm doing well, thank you for asking. I'm here to help with any questions or conversations you'd like to have. How can I assist you today?
You: exit
```

## License

This project is open source and available under the MIT License.