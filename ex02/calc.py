import tkinter as tk;
import tkinter.messagebox as tkm;

i=9;
x=0
y=0

root = tk.Tk()

root.title("電卓");
root.geometry("300x500");

for i in range(9, -1, -1):
    button = tk.Button(root, font = ("", 30), text=i, width=4, height=2);
    button.grid(row = x,column = y);
    y += 1;
    
    if y%3==0:
        x += 1;
        y=0
        
    
    

root.mainloop();
    