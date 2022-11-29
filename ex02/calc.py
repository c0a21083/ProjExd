import tkinter as tk;
import tkinter.messagebox as tkm;

i=9;
x=1
y=0

root = tk.Tk()

root.title("電卓");
root.geometry("300x500");

entry = tk.Entry(root, justify="right", width=10, font=("",40));
entry.grid(row=0, column=0, columnspan=3);

def button_click(event):
    btn = event.widget;
    num = btn["text"];
    #entry.insert(tk.END, num);
    #tkm.showinfo("押しましたね", f"{num}のボタンが押されました");
    
    if num == "=":
        pass
    else:
        entry.insert(tk.END, num)

for i in range(9, -1, -1):
    button = tk.Button(root, font = ("", 30), text=f"{i}", width=4, height=2);
    button.bind("<1>", button_click);
    button.grid(row = x,column = y);
    y += 1;
    
    if y%3==0:
        x += 1;
        y=0
        
    
    
operators = ["+", "="];

for ope in operators:
    button = tk.Button(root, text = f"{ope}", width=4, height=2, font = ("", 30));
    button.grid(row=x, column=y)
    y += 1;
    if y%3==0:
        x += 1;
        y=0;

root.mainloop();
    