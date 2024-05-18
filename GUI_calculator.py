import tkinter as tk

def set_mode(mode):
    global conversion_mode
    conversion_mode = mode
    entry.delete(0, tk.END)
    mode_label.config(text=f"Mode: {'Integer' if mode == 'i' else 'Float'}")

def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + key)

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        if conversion_mode == "i":
            result = int(result)  # Force integer result if conversion mode is integer
        else:
            result = float(result)  # Ensure float result if conversion mode is float
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def center_window(root, width=400, height=500):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

root = tk.Tk()
root.title("Calculator")

conversion_mode = "f"  # Default mode is float

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=4)

mode_label = tk.Label(root, text="Mode: Float", font=('Arial', 14))
mode_label.grid(row=1, column=0, columnspan=2)

tk.Button(root, text='Integer', font=('Arial', 14), command=lambda: set_mode('i')).grid(row=1, column=2)
tk.Button(root, text='Float', font=('Arial', 14), command=lambda: set_mode('f')).grid(row=1, column=3)

buttons = [
    '7', '8', '9', '/', 
    '4', '5', '6', '*', 
    '1', '2', '3', '-', 
    '0', '.', '=', '+', 
    '%'
]

row = 2
col = 0

for button in buttons:
    action = lambda x=button: press(x) if x != '=' else evaluate()
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=clear).grid(row=row, column=0)
tk.Button(root, text='←', padx=20, pady=20, font=('Arial', 18), command=backspace).grid(row=row, column=1)

# Set max width, center the window, and disable resizing
max_width = 310
center_window(root, width=max_width)
root.resizable(False, False)

root.mainloop()
