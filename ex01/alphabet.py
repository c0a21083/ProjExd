if __name__ == "__main__":
    import datetime
    import random

    in_st = 0;
    out_st = 2;
    ans = 0;
    count = 0;
    size = 1;
    ans1 = 1;

    alpha = ["A","B","C","D","E","F","G","H","I","J",\
        "K","L","M","N","O","P","Q","R","S","T",\
        "U","V","W","X","Y","Z"]
    
    
    
    

    while ans == 0:
        while size>0:
            in_st = random.randint(1,27);
            if in_st > out_st:
                size = 0;
            else:
                size = 1;
        in_list = random.sample(alpha,in_st);
        out_list = random.sample(in_list,out_st);
        print("対象文字: ");
        for i in range(in_st):
            print(in_list[i] + " ",end="")
        print("\n")
        for l in out_list:
            in_list.remove(l);
        print("表示文字:");
        for i in range(in_st - out_st):
            print(in_list[i] + " ",end="")
        print("\n")
        while ans1>0:
            num = int(input("欠損文字数は？"));
            if num == out_st:
                print("正解!")
                ans1 = 0;
            else:
                print("不正解");
                ans1 = 1;
        print("具体的な欠損文字は？");        
        a_1 = input("1つめの文字を入力してください:");
        a_2 = input("2つめの文字を入力してください:");
        if a_1 in out_list and a_2 in out_list:
            print("正解！");
            ans = 1;
        else:
            print("残念");
            ans = 0;
        count += 1;
    print(str(count) + "回で終了しました。");
    
    