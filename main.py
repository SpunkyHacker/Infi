import tkinter as tk
import webbrowser

class QuickAccessAssistant(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Infi")
        self.geometry("500x100")
        self.configure(padx=20, pady=20)

        self.prompt_entry = tk.Entry(self, font=("Segoe UI", 14))
        self.prompt_entry.pack(fill=tk.X)
        self.prompt_entry.focus_set()
        self.prompt_entry.bind("<Return>", self.on_enter_press)

        self.result_text = None  # Will create only on error

    def on_enter_press(self, event):
        self.process_prompt()

    def process_prompt(self):
        prompt = self.prompt_entry.get()
        if prompt.lower().startswith("search "):
            query = prompt[7:]
            webbrowser.open(f"https://www.google.com/search?q={query}")
            self.destroy()  # Close app on success
        else:
            if not self.result_text:
                self.result_text = tk.Text(self, height=8, font=("Segoe UI", 12))
                self.result_text.pack(fill=tk.BOTH, expand=True, pady=(10, 0))
            self.result_text.insert(tk.END, "Unknown command.\n")
            self.prompt_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = QuickAccessAssistant()
    app.mainloop()
