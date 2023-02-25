from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

#まずはスクレイピング．
Fuji = webdriver.Chrome("chromedriver")

#藤井くんの勝敗のサイトを開く
Fuji.get('https://shogi-sanpo.com/fujiisouta/result/')
time.sleep(1)

win = Fuji.find_elements(By.CLASS_NAME , "gourmetWin")
lose = Fuji.find_elements(By.CLASS_NAME , "gourmetLose")

#データを抜き取ってくる
data = []
for _ in win:
    if _.text != "":
        data.append(_.text.replace("\n" , ""))
#        print(_.text)
for _ in lose:
    if _.text != "":
        data.append(_.text.replace("\n" , ""))
#        print(_.text)

#勝1，負0のリスト作成．
win = []
for _ in range(len(data)):
    if data[_][-1] == "勝":
        win.append(1)
    else:
        win.append(0)

#先手1，後手0のリスト作成．
first = []
check = []
for _ in range(len(data)):
    for __ in range(len(data[_])):
        if data[_][__] == "[":
            check.append(data[_][__ + 1])
for ___ in range(len(check)):
    if check[___] == "先":
        first.append(1)
    else:
        first.append(0)

#相手の段位が七段以下1，八段以上0のリスト作成．
opp = []
kakunin = []
danni = ["四段" , "五段" , "六段" , "七段"]
for _ in range(len(data)):
    for __ in range(len(data[_]) - 10):
        for ___ in danni:
            if data[_][__] + data[_][__ + 1] == ___:
                kakunin.append(1)
            else:
                kakunin.append(0)
    opp.append( max(kakunin) )
    kakunin.clear()

#pandasでデータフレームにする．
df = pd.DataFrame({
    "win":win,
    "first":first,
    "opp":opp
})
print(df)

#csvファイルにしてエクスポート
df.to_csv("Fuji.csv" , encoding = "shift-jis")
