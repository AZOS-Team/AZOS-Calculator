import tkinter as tk

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.result = 0
        self.entry_text = tk.StringVar()
        self.entry_text.set("")
        self.entry = tk.Entry(self.root, textvariable=self.entry_text, width=25)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        button_texts = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "+", "="]

        for i, text in enumerate(button_texts):
            row = i // 4 + 1
            column = i % 4
            button = tk.Button(self.root, text=text, width=5, height=2, command=lambda text=text:self.on_button_click(text))
            button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, text):
        if text == "C":
            self.result = 0
            self.entry_text.set("")
        elif text == "=":
            try:
                self.result = eval(self.entry_text.get())
                self.entry_text.set(str(self.result))
            except:
                self.entry_text.set("Error")
        else:
            if self.entry_text.get() == "Error":
                self.entry_text.set("")
            self.entry_text.set(self.entry_text.get() + text)

    def run(self):
        self.root.mainloop()

calculator = Calculator()
calculator.run()
