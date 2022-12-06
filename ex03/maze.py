<<<<<<< HEAD
import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
=======
import tkinter as tk;
import maze_maker as mm;
import tkinter.messagebox as me;
import random;

#ボタン押下中
def key_down(event):
    global key
    key = event.keysym
    ranx = random.randint(0,15);
    rany = random.randint(0,9);
    
#ボタン非接触時
>>>>>>> ex
def key_up(event):
    global key
    key = ""

<<<<<<< HEAD

def main_proc():
    global mx, my;
    global cx, cy;
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1:
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx, cy = mx*100+50, my*100+50;
    canvas.coords("kokaton", cx, cy)
    root.after(100, main_proc)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    mx, my = 1, 1;
    cx, cy = mx*100+50, my*100+50;
    tori = tk.PhotoImage(file="../fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
=======
#キャラ移動
def main_proc():
    global mx, my;
    global cx, cy;
    global count, ranx, rany;
    if key == "Up":
        my -= 1
        ranx = random.randint(0,15);
        rany = random.randint(0,9);
    if key == "Down": 
        my += 1
        ranx = random.randint(0,15);
        rany = random.randint(0,9);
    if key == "Left": 
        mx -= 1
        ranx = random.randint(0,15);
        rany = random.randint(0,9);
    if key == "Right": 
        mx += 1
        ranx = random.randint(0,15);
        rany = random.randint(0,9);
    if maze_lst[mx][my] == 1:
        if key == "Up": 
            my += 1
            count += 1
        if key == "Down": 
            my -= 1
            count += 1
        if key == "Left": 
            mx += 1
            count += 1
        if key == "Right": 
            mx -= 1
            count += 1
    cx, cy = mx*100+50, my*100+50;
    canvas.coords("kokaton", cx, cy)
    if cx==gx and cy==gy:
        me.showinfo("dead","GameOver")
        root.mainloop()
    if 1100<=cx<=1400 and 750<=cy<=800:
        me.showinfo("goal", "GOOOOOOOOAL!!!!");
        root.mainloop();
                    
        
    root.after(100, main_proc)
    
def enemy_move():
    global gx, gy;
    global ranx, rany;
    ranx = random.randint(0,15);
    rany = random.randint(0,9);
    gx, gy = ranx*100+50, rany*100+50;
    canvas.coords("ene", gx, gy);
    



if __name__ == "__main__":
    count = 0;
    ranx, rany = 0, 0
    root = tk.Tk()
    root.title("迷えるこうかとん")
    #windowの描写
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    
    #迷路用リスト作成
    maze_lst = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_lst)
    #マスの座標
    mx, my = 1, 1;
    #キャラの座標
    cx, cy = mx*100+50, my*100+50;
    gx, gy = 0, 0
    enemy = tk.PhotoImage(file = "./マスターハンド.png");
    #gx, gy = ranx*100+50, rany*100+50;
    enemy_move()
    canvas.create_image(gx, gy, image = enemy, tag = "ene");
    #登場キャラ、スタートゴールの画像
    tori = tk.PhotoImage(file="../fig/8.png")
    start = tk.PhotoImage(file = "./start.png");
    goal = tk.PhotoImage(file = "./goal.png");
    enemy = tk.PhotoImage(file = "./マスターハンド.png");
    
    #キャンバス内に表示
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    canvas.create_image(150, 50, image = start, tag = "sta");
    canvas.create_image(1200, 750, image = goal, tag = "gol");
    canvas.create_image(gx, gy, image = enemy, tag = "ene");
    key = ""
    #イベント設定
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    enemy_move()
    
>>>>>>> ex
    root.mainloop()