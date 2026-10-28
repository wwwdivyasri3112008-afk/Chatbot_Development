# Week 9 - Chatbot Development Using Ollama and Python

## Objective

To develop a command-line AI chatbot using Python and Ollama. The chatbot maintains conversation history and saves interactions for future analysis and LangChain integration.

## Technologies Used

- Python
- Ollama
- Llama 3
- Pandas
- Jupyter Notebook

## Features

1. Local AI chatbot using Ollama.
2. Context-aware conversations using conversation history.
3. Automatic logging of user messages and chatbot responses.
4. CSV-based chat history storage.
5. Sample question and response datasets.
6. Jupyter Notebook for testing and evaluation.

## Project Structure

```text
Chatbot_Development/
├── dataset/
│   ├── chat_history.csv
│   ├── sample_questions.csv
│   ├── chatbot_logs.txt
│   └── responses.csv
├── notebook/
│   └── Week9_Chatbot_Development.ipynb
├── chatbot.py
├── README.md
└── requirements.txt
```

## Installation

### Step 1: Install Ollama

Download Ollama from https://ollama.com/download.

### Step 2: Download the Model

Run the following command:

```bash
ollama pull llama3
```

### Step 3: Install Python Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the Chatbot

```bash
python chatbot.py
```

### Step 5: Exit the Chatbot

Type `exit`, `quit`, or `q`.

## Dataset Description

- `chat_history.csv`: Stores timestamps, roles, and messages.
- `sample_questions.csv`: Contains sample chatbot questions.
- `chatbot_logs.txt`: Stores conversations in text format.
- `responses.csv`: Contains example questions and responses.

## Evaluation

The chatbot can be evaluated by testing different questions, checking response generation, verifying conversation history, and confirming that interactions are saved correctly.

## Future Enhancement

LangChain can be integrated to improve conversation management and support additional language-model workflows.

## Conclusion

This project demonstrates how to build a basic local AI chatbot using Python and Ollama, maintain conversation history, and store interaction logs for future development.