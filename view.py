import tkinter as tk

class View:
    def __init__(self, root, controller, model):
        self.root = root
        self.controller = controller
        self.model = model

        # Setup window properties
        self.root.title("D&D Toolkit")
        self.root.geometry("900x600")
        
        # Display the message from the model
        self.label = tk.Label(self.root, text=self.model.message, font=("Arial", 16))
        self.label.pack(padx=20, pady=20)
