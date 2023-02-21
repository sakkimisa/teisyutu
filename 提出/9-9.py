#引数で受け取った半径の円の円周を計算して返す関数(メソッド)と、引数で受け取った半径の円の面積を計算して返す関数(メソッド)を定義する。
# 2 つの関数(メソッド)の引数は実数でも受け取れるものとします。
# その関数(メソッド)を利用し、円周率は正しい値を用いることとし、計算結果は小数第 3 位以下を切り捨てとします。

import math
pi = 3.14159

def cir(cir_num):
    #cir_num = radius_num
    cir_result = 2 * cir_num * pi
    cir_result = math.floor(cir_result * 10 ** 2) / (10 ** 2)
    
    return cir_result

def area(area_num):
    #area_num = radius_num
    area_result = pi * area_num ** 2
    area_result = math.floor(area_result * 10 ** 2) / (10 ** 2)
    
    return area_result


radius_num = float(input("半径を入力してください："))
cir_result_num = cir(radius_num)
area_result_num = area(radius_num)

print("半径",radius_num,"の円の円周は",cir_result_num,sep="")
print("半径",radius_num,"の円の面積は",area_result_num,sep="")


