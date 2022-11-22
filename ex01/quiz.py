import random


def shutudai(qa_list):
    qa = random.choice(qa_list)
    print("問題:" + qa["q"])
    return qa["a"]
    
def kaitou(ans_list):
    ans = input("答えるのだ:")
    


if __name__ == "__main__":
    qa_list = [
        {"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]}
        {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]}
        {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"]}
    ]
    shitudai(qa_list)
    kaitou(ans_list)