import tkinter as tk;
import tkinter.messagebox as tkm;
import math;

i=9;
x=1;
y=0;


root = tk.Tk()

root.title("電卓");
root.geometry("500x700");



entry = tk.Entry(root, justify="right", width=15, font=("",40));
entry.grid(row=0, column=0, columnspan=5);

def button_click(event):
    btn = event.widget;
    num = btn["text"];
    #entry.insert(tk.END, num);
    #tkm.showinfo("押しましたね", f"{num}のボタンが押されました");
    
    if num == "=":
        siki = entry.get();
        #先頭の文字が数字でない場合の場合、エラー表示をする。
        if siki[0] == "+" or "-" or "/" or "*" or "!" or "E" or "r" or "o":
            entry.delete(0, tk.END);
            entry.insert(tk.END, "Error!");
        #特定の値を入力で、特別な表示を行う。
        if siki == "18782+18782":
            tkm.showwarning("警告", "恐ろしい人間ですね");
        
        #クリスマス（未完成）
        #elif siki == "1224+1225" or "1225+1224":
            #tkm.showinfo("ハッピー！","Merry Christmas!");
            #entry.delete(0, tk.END);
            #entry.insert(tk.END, "Merry Christmas!");
        
        #階乗の計算（未完成のため、1けたのみ可能）
        leng = len(siki);
        if siki[leng-1] == "!":
            ans = math.factorial(int(siki[0,leng-2]));
            entry.delete(0, tk.END);
            entry.insert(tk.END, ans);
        else:
            ans = eval(siki);
            entry.delete(0, tk.END);
            entry.insert(tk.END, ans);
    #1文字削除
    elif num == "C":
        siki = entry.get();
        leng = len(siki);
        entry.delete(leng-1, tk.END);    
    #全て削除
    elif num == "AC":
        entry.delete(0, tk.END);
    else:
        entry.insert(tk.END, num)

#数字ボタンの表示
for i in range(9, -1, -1):
    button = tk.Button(root,text=f"{i}", width=4, height=3, font = ("", 30));
    button.bind("<1>", button_click);
    button.grid(row = x,column = y);
    y += 1;
    
    if y%3==0:
        x += 1;
        y=0;
        
#計算記号ボタンの表示-1
calc = ["/", "*", "**2", "**", "!"];
for ca in calc:
    button = tk.Button(root,text=f"{ca}", width=4, height=3, font = ("", 30));
    button.bind("<1>", button_click);
    button.grid(row = x,column = y);
    y += 1;
    
    if y%3==0:
        x += 1;
        y=0;
    
    
    
        
    
#計算記号ボタンの表示-2
operators = ["C", "AC", "+", "-", "="];
x=1;
for ope in operators:
    
    button = tk.Button(root, text = f"{ope}", width=5, height=3, font = ("", 30));
    button.bind("<1>", button_click);
    button.grid(row=x, column=3)
    x += 1;
        

root.mainloop();
    