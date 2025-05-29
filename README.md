# Gemini Multi-Turn Chat Console Script

This Python script provides an interactive multi-turn chatbot using the **Google Gemini API (Free Tier)** via the official `google-generativeai` SDK. It allows the user to carry on a conversation with the Gemini model via the console and summarizes the entire conversation at the end.

---

## 🚀 Features

- Multi-turn chat: Keeps the full conversation context.
- Dynamic model creativity: Adjust `temperature` to influence the style of responses.
- Secure API key management using `.env` file.
- Clean console-based user interface.

---

## 🧠 What This Script Does

1. Prompts the user to enter a **temperature** value (controls creativity of responses).
2. Starts a **chat session** with the Gemini model.
3. Accepts **multiple user inputs** (until user types `done`).
4. Maintains the conversation context across turns.
5. At the end, asks Gemini to **summarize the conversation** and prints the final response.

---

## 🛠️ Setup & Installation

### 1. Clone or Download the Script

```bash
git clone https://github.com/shubham587/gemini-multi-turn-chat.git
cd gemini-multi-turn-chat
```
###
### 2. Install Dependencies

    You’ll need:
    
    - Python 3.7+
    - `google-generativeai
    - `python-dotenv`
    
    Install with pip:
    pip install google-generativeai python-dotenv
###
### 3. Run py file with Python
    ```bash
    python gemini-multi-turn-chat.py
    ```
