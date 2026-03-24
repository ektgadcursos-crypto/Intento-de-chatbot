import tkinter as tk
from tkinter import messagebox

# Placeholder: Replace this with actual database fetching logic
def fetch_articles():
    # This function should connect to the database and retrieve articles
    return [
        {"title": "Article 1", "content": "Content of Article 1"},
        {"title": "Article 2", "content": "Content of Article 2"},
        # Add all articles here
    ]

# GUI Application Class
class Ley62022Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Ley 6/2022 Chatbot")

        self.label = tk.Label(master, text="Welcome to Ley 6/2022 Chatbot")
        self.label.pack()

        self.fetch_button = tk.Button(master, text="Fetch Articles", command=self.display_articles)
        self.fetch_button.pack()

    def display_articles(self):
        articles = fetch_articles()
        article_list = "\n".join([f"{article['title']}: {article['content']}" for article in articles])
        messagebox.showinfo("Articles", article_list)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_app = Ley62022Chatbot(root)
    root.mainloop()