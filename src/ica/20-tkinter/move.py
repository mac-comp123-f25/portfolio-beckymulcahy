import tkinter as tk

# ----- GUI class and methods -----
class BasicGui:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin.title("Basic GUI")

        self.titleLabel = tk.Label(self.mainWin, text="My Basic Gui ", font=("Arial", 16))
        self.titleLabel.pack(pady=10)

        self.myCanvas = tk.Canvas(self.mainWin, bg="blue")
        self.myCanvas.pack(fill=tk.BOTH, expand=True)

        self.textID = self.myCanvas.create_text(
            150, 100,
            text="Hello",
            font=("Arial", 20, "bold"),
            fill="lightblue"
        )

        self.mainWin.bind("<w>", self.move_callback)
        self.mainWin.bind("<a>", self.move_callback)
        self.mainWin.bind("<s>", self.move_callback)
        self.mainWin.bind("<d>", self.move_callback)

        # Arrow keys
        self.mainWin.bind("<Up>", self.move_callback)
        self.mainWin.bind("<Down>", self.move_callback)
        self.mainWin.bind("<Left>", self.move_callback)
        self.mainWin.bind("<Right>", self.move_callback)




        self.quitButton = tk.Button(self.mainWin, text="Quit", command=self.mainWin.quit)
        self.quitButton.pack(pady=10)

    def move_callback(self, event):
        key_pressed = event.keysym
        print("Key pressed:", key_pressed)

        if key_pressed in ("w", "Up"):
            self.myCanvas.move(self.textID, 0, -10)
        elif key_pressed in ("a", "Left"):
            self.myCanvas.move(self.textID, -10, 0)

        elif key_pressed in ("s", "Down"):
            self.myCanvas.move(self.textID, 0, 10)

        elif key_pressed in ("d", "Right"):
            self.myCanvas.move(self.textID, 10, 0)

    def run(self):
        self.mainWin.mainloop()


# ----- Main program -----
myGui = BasicGui()
myGui.run()

