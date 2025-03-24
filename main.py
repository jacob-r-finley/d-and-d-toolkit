import tkinter as tk
from view import View
from controller import Controller

# Model: holds the data
class Model:
    def __init__(self):
        self.message = "Hello World"

def main():
    root = tk.Tk()
    
    # Instantiate MVC components
    model = Model()
    controller = Controller(model)
    view = View(root, controller, model)
    
    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
