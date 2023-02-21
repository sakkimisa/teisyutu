#引数で受け取った体重(㎏)と身長(cm)から BMI 値を計算して返す関数(メソッド)と、同様に適正体重を計算して返す関数(メソッド)を定義する。
# 2 つの関数(メソッド)の引数は実数でも受け取れるものとします。
# その関数(メソッド)を利用して、ユーザーが画面に入力した身長(cm)と体重(㎏)から BMI 値と適性体重を表示するプログラムを作成しなさい。なお、計算結果は小数第 3 位以下を切り捨てとします。
#注）
#• BMI ＝ 体重 kg ÷ (身長 m)2
#• 適正体重 ＝ (身長 m)2 × 22

import math

def bmi(height_num,weight_num):
    bmi_result = weight / (height/100)**2
    bmi_result = math.floor(bmi_result * 10 ** 2) / (10 ** 2)
    
    return bmi_result

def normal_weight(height_num,weight_num):
    normal_weight_result = (height/100)**2 *22
    normal_weight_result = math.floor(normal_weight_result * 10 ** 2) / (10 ** 2)
    
    return normal_weight_result
    
height = float(input("身長(cm)を入力してください："))
weight = float(input("体重(kg)を入力してください："))

bmi_result_num = bmi(height,weight)
normal_weight_result_num = normal_weight(height,weight)

print("BMI値は",bmi_result_num,"です",sep="")
print("適正体重は",normal_weight_result_num,"kgです",sep="")
