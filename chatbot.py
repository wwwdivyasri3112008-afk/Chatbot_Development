import os
import csv
from datetime import datetime
import ollama

MODEL_NAME = "llama3"

LOG_FILE = "dataset/chatbot_logs.txt"
HISTORY_CSV = "dataset/chat_history.csv"


def initialize_files():
    os.makedirs("dataset", exist_ok=True)

    if not os.path.exists(HISTORY_CSV) or os.path.getsize(HISTORY_CSV) == 0:
        with open(HISTORY_CSV, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Role", "Message"])


def log_interaction(role, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {role.upper()}: {message}\n")

    with open(HISTORY_CSV, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, role, message])


def run_chatbot():
    initialize_files()

    print(f"--- AI Chatbot Started ({MODEL_NAME}) ---")
    print("Type 'exit' to stop the chatbot.\n")

    conversation_history = []

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit", "q"]:
                print("Chatbot: Goodbye!")
                break

            conversation_history.append({
                "role": "user",
                "content": user_input
            })

            log_interaction("user", user_input)

            print("Chatbot is thinking...")

            response = ollama.chat(
                model=MODEL_NAME,
                messages=conversation_history
            )

            bot_response = response["message"]["content"]

            print(f"Chatbot: {bot_response}\n")

            conversation_history.append({
                "role": "assistant",
                "content": bot_response
            })

            log_interaction("assistant", bot_response)

        except KeyboardInterrupt:
            print("\nChatbot: Session ended.")
            break

        except Exception as error:
            print(f"\nError: {error}")
            print("Check whether Ollama is installed and the llama3 model is available.")
            break


if __name__ == "__main__":
    run_chatbot()