import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        quit_button= tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)
        quit_button.grid (row=0, column=0)

        hello_button = tk.Button(self.mainWin, text="Hello", command=self.mainWin.destroy)
        hello_button.grid (row=1, column=0)

        goodbye_button = tk.Button(self.mainWin, text="Goodbye", command=self.mainWin.destroy)
        goodbye_button.grid (row=2, column=0)

        self.welcome_label = tk.Label(self.mainWin, text="Welcome")
        self.welcome_label.grid (row=1, column=1)

    def run(self):
        self.mainWin.mainloop()

    def quit_callback(self):
        self.mainWin.destroy()

    def hello_callback(self):
        self.welcome_label.configure(text="Hello")

    def goodbye_callback(self):
        self.welcome_label.configure(text="Goodbye")


# ----- Main program -----
myGui = BasicGui()
myGui.run()

