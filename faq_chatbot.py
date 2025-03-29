import tkinter as tk
from fuzzywuzzy import process

# FAQ dataset
faq_data = {
    "hello": "Hi there! How can I help you?",
    "how are you": "I'm just a bot, but I'm doing great! 😊",
    "bye": "Goodbye! Have a great day! 👋",
    "what can you do": "I can answer some frequently asked questions. Try asking me something!",
    "who created you": "I was created by a Python enthusiast!",
    "What is your name?": "I am a chatbot!",
    "How can I contact support?": "You can email support at support@example.com.",
    "What are your working hours?": "We are available 24/7!",
    "Where is your office located?": "Our office is in Mumbai, India.",
    "Do you support international shipping?": "Yes! We ship worldwide.",
    "How can I reset my password?": "Click on 'Forgot Password' on the login page to reset it.",
    "What payment methods do you accept?": "We accept credit cards, PayPal, and UPI.",
    "How long does delivery take?": "Standard delivery takes 5-7 business days."
}

# Function to get the best-matching response
def get_response(user_input):
    best_match, score = process.extractOne(user_input, faq_data.keys())
    return faq_data[best_match] if score > 50 else "Sorry, I don't understand that question."

# Function to handle user input
def send_message():
    user_text = entry.get().strip()
    if user_text:
        chat_log.insert(tk.END, "You: " + user_text + "\n", "user")
        bot_response = get_response(user_text)
        chat_log.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")
        entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("400x500")

# Chat Display
chat_log = tk.Text(root, bg="white", font=("Arial", 12), wrap=tk.WORD)
chat_log.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_log.tag_configure("bot", foreground="green", font=("Arial", 12, "italic"))
chat_log.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Input Field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5, padx=10, fill=tk.X)

# Send Button
send_btn = tk.Button(root, text="Send", font=("Arial", 12, "bold"), command=send_message)
send_btn.pack(pady=5)

root.mainloop()
