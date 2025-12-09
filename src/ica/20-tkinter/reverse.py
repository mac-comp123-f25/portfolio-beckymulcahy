import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Reverse Strings")

        label1 = tk.Label(self.mainWin, text="Type of phrase to reverse")
        label1.grid(row=0, column=0, padx=10, pady=10)

        self_entry_box = tk.Entry(self.mainWin, width=25)
        self_entry_box.grid(row=0, column=1, padx=10, pady=10)

        self.entry_box.bind("<Return>", self.entry_response)

        self.display_label= tk.Label(self.mainWin, text="Text will appear")
        self.display_label.grid(row=1, column=0, columnspan= 2, pady=10)

        quit_button = tk.Button(self.mainWin, text="Quit", command=self.mainWin.destroy)
        quit_button.grid(row=2, column=0, columnspan=2, pady=10)


    def run(self):
        self.mainWin.mainloop()

    def entry_response(self, event):
        user_input= self.entry_box.get()
        self.display_label.configure(text=f"you entered: {user_input}")


# ----- Main program -----
myGui = BasicGui()
myGui.run()

