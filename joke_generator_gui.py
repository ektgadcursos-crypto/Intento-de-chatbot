import tkinter as tk
import random

class JokeGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title('Joke Generator')
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
            "Why don’t skeletons fight each other? They don’t have the guts!",
            "What do you get when you cross a snowman with a vampire? Frostbite!"
        ]
        self.favorites = []

        self.joke_label = tk.Label(self.master, text='Click the button for a joke!', wraplength=300)
        self.joke_label.pack(pady=20)

        self.get_joke_button = tk.Button(self.master, text='Get Joke', command=self.get_joke)
        self.get_joke_button.pack(pady=5)

        self.save_joke_button = tk.Button(self.master, text='Save Favorite Joke', command=self.save_joke)
        self.save_joke_button.pack(pady=5)

        self.clear_button = tk.Button(self.master, text='Clear Screen', command=self.clear_screen)
        self.clear_button.pack(pady=5)

        self.exit_button = tk.Button(self.master, text='Exit', command=self.master.quit)
        self.exit_button.pack(pady=5)

    def get_joke(self):
        joke = random.choice(self.jokes)
        self.joke_label.config(text=joke)

    def save_joke(self):
        current_joke = self.joke_label.cget('text')
        if current_joke not in self.favorites:
            self.favorites.append(current_joke)
            self.joke_label.config(text='Favorite Joke Saved!')
        else:
            self.joke_label.config(text='Joke already saved.')

    def clear_screen(self):
        self.joke_label.config(text='')

if __name__ == '__main__':
    root = tk.Tk()
    app = JokeGenerator(root)
    root.mainloop()