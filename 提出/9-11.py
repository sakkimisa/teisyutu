#1 から 4 までの整数の乱数を発生させ、その乱数を返す関数(メソッド)を定義し、その関数(メソッド)を利用して、今日の運勢を下記の実行例のように表示するプログラムを作成する。
# 乱数が 1 のとき絶好調、2 のとき好調、3 のとき不調、4 のとき絶不調と表示します。

import random

def luck():
   random_num = random.randint(1,4)
   
   return random_num

if  luck() == 1:
    print("本日の運勢：絶好調")

elif luck() == 2:
    print("本日の運勢：好調")

elif luck() == 3:
    print("本日の運勢：不調")

else :
    print("本日の運勢：絶不調")



