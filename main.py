import tkinter as tk
from tkinter import ttk
import pandas as pd
from io import StringIO

# DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) 

# Root window
root = tk.Tk()

# Buttons frame
button_frame = ttk.Frame(root)
button_frame.pack()

# Output text box
output_text = tk.Text(root, height=10)
output_text.pack(fill=tk.BOTH, expand=True)

# Capture output
def get_output(func):
  buffer = StringIO()
  func(buf=buffer)
  return buffer.getvalue()

# Update display
def display_output(text):
  output_text.delete('1.0', tk.END)
  output_text.insert(tk.END, text)

# Create buttons  
buttons = [('Info', lambda: display_output(get_output(df.info))),
           ('Describe', lambda: display_output(df.describe())),
           ('Sum', lambda: display_output(df.sum()))]
           
for text, func in buttons:
    btn = ttk.Button(button_frame, text=text, command=func)
    btn.pack(side= tk.LEFT, fill=tk.BOTH)  

root.mainloop()