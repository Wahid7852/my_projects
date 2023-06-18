import tkinter as tk
from tkinter import ttk
import psycopg2
import datetime
import pyjokes

user = 'User'

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="root",
    host="localhost",
    port='5432'
)

curser = conn.cursor()

curser.execute('''CREATE TABLE IF NOT EXISTS chat_history (
                id SERIAL PRIMARY KEY,
                message TEXT,
                response TEXT
              )''')

actions = {
    'hi': 'Hello, how can I assist you today?',
    'greeting': 'Hello, how can I assist you today?',
    'goodbye': 'Goodbye! Have a nice day.',
    'what is your name?': 'I am your personal chatbot. Nice to meet you',
    'What is the wather?': 'I am a chatbot, not a weather bot.',
    'what is your age? ': 'I am a chatbot, I have no age.',
    'favourite music': 'I like all kinds of music.',
    'favourite movie': 'Robot 2010',
    'favourite food': 'I am a chatbot, I do not eat food.',
    'what is your hobby? ': 'learning new things and chatting with people like you.',
    'what is the time?': str(datetime.datetime.now()),
    'what is the date?': str(datetime.date.today()),
    'favourite sport': 'cricket',
    'tell me a joke ?': str(pyjokes.get_joke()),
    'what is your favourite color?': 'I like all colors.',
    'what is your favourite book?': 'I like all books.',
    'what is your favourite game?': 'I like all games.',
    'what is your favourite subject?': 'I like all subjects.',

}


root = tk.Tk()
root.title("Conversation App With Cloud Database")
root.geometry("400x500")

chat_history = tk.Text(root)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


cur = conn.cursor()
cur.execute("SELECT * FROM chat_history")
rows = cur.fetchall()
for row in rows:
    chat_history.insert(tk.END, "You: " + row[1] + "\n")
    chat_history.insert(tk.END, "Chatbot: " + row[2] + "\n")

# press enter to input
root.bind('<Return>', lambda e: handle_user_message())

user_input = ttk.Entry(root, width=80)
user_input.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

send_button = ttk.Button(root, text="Send")
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

clear_button = ttk.Button(root, text="Clear Chat History")

clear_button = ttk.Button(root, text="Clear Chat History")
clear_button.pack(side=tk.BOTTOM, padx=10, pady=10)

def handle_user_message():
    
    message = user_input.get().strip()
    if message == 'clear':
        clear_chat_history()
        user_input.delete(0, tk.END)
        return
    if message == 'help':
        # open questions file as new file
        with open('questions.txt', 'r') as file:
            # read file
            data = file.read()
            # show file data in chat history
            chat_history.insert(tk.END, data + "\n")
    if 'time' in message:
        return str(datetime.datetime.now())
    if 'date' in message:
        return str(datetime.date.today())
    if 'joke' in message:
        return str(pyjokes.get_joke())
    if 'weather' in message:
        return 'I am a chatbot, not a weather bot.'
    if 'name' in message:
        return f'Hello {user}, I am your personal chatbot. Nice to meet you'
    if 'age' in message:
        return 'I am a chatbot, I have no age.'
    if 'hobby' in message:
        return 'learning new things and chatting with people like you.'
    if 'food' in message:
        return 'I am a chatbot, I do not eat food.'
    if 'music' in message:
        return 'I like all kinds of music.'
    if 'movie' in message:
        return 'Robot 2010'
    if 'sport' in message:
        return 'cricket'
    if 'color' in message:
        return 'I like all colors.'
    if 'book' in message:
        return 'I like all books.'
    if 'game' in message:
        return 'I like all games.'

    chat_history.insert(tk.END, "You: " + message + "\n")

    
    response = get_chatbot_response(message)

    
    chat_history.insert(tk.END, "Chatbot: " + response + "\n")

    
    cur.execute("INSERT INTO chat_history (message, response) VALUES (%s, %s)", (message, response))
    conn.commit()

    
    user_input.delete(0, tk.END)

def get_chatbot_response(message):
    
    for action, response in actions.items():
        if message.lower().startswith(action):
            return response
        if message == 'help':
            return "Please use questions given above."
        
    
    return "I'm sorry, I didn't understand that. Please use questions from the supplied file."


def clear_chat_history():
    chat_history.delete('1.0', tk.END)
    cur = conn.cursor()
    cur.execute("DELETE FROM chat_history")
    conn.commit()


clear_button.configure(command=clear_chat_history)


send_button.configure(command=handle_user_message)


root.mainloop()


cur.close()
conn.close()
