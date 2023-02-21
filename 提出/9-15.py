#複数人分の名前と 3 教科分の得点のデータを連想配列の引数として受け取り、各人の平均点と教科ごとの平均点を下記の実行例のように表示をする関数(メソッド)を定義する
#平均点は小数第 3位を切り捨てとし、その関数(メソッド)を利用して、end と入力されたら、それまで入力されていた各人の平均点、教科ごとの平均点を表示するプログラム

import math

def info_num(score_num):
    sub_score1 = 0
    sub_score2 = 0
    sub_score3 = 0
    
    index = 0
    score_sum = 0
    
    for name,num_array in score_num.items():
        
        for score in num_array:
            score_sum += score
        
            if index == 0:
                sub_score1 += score
            
            elif index == 1:
                sub_score2 += score
                
            elif index == 2:
                sub_score3 += score
            
            index += 1
    
        person_num = score_sum / len(num_array)
        person_num = math.floor(person_num * 10 ** 2) / (10 ** 2)
        print(name,"さんの平均点は",person_num,"です。")
    
    sub_ave = sub_score1 /len(score_num)
    print("１教科目の平均点は",math.floor(sub_ave * 10 ** 2) /  (10 ** 2),"です。")
    sub_ave = sub_score2 /len(score_num)
    print("２教科目の平均点は",math.floor(sub_ave * 10 ** 2) /  (10 ** 2),"です。")
    sub_ave = sub_score3 /len(score_num)
    print("３教科目の平均点は",math.floor(sub_ave * 10 ** 2) /  (10 ** 2),"です。")
                
        
                        
        



info_dict = {}

no = 1
while True:
    name = input(str(no) + "人目の名前を入力してください：")
    
    if name == "end" :
        break
    
    score1 = int(input(str(no) + "人目の１教科目の点数を入力して下さい："))
    score2 = int(input(str(no) + "人目の２教科目の点数を入力して下さい："))
    score3 = int(input(str(no) + "人目の３教科目の点数を入力して下さい："))
    info_dict[name] = [score1,score2,score3]
    
    
    no += 1
    

info_num(info_dict)
    
            
        