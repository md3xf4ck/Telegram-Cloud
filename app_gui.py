from tkinter import Tk, Label
def init():
    tk = Tk()
    tk.title("Telegram Cloud")
    tk.geometry("400x200")

    AppName = Label(tk, text="Telegram Cloud", font=("Arial", 16), foreground="blue")
    AppName.pack(pady=20)

    return tk

if __name__ == "__main__":
    tk = init()
    tk.mainloop()
