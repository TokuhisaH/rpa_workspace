import pyautogui as pag
import pyocr
from PIL import Image
import sys
import subprocess

import pyperclip
import os
import time

#acrobat readerを使ってpdf開くのでacrobat readerの実行ファイルの場所を記述する
acr_path="C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"

#開くファイルのパス
openfile_path="data/lec_rpa/todokede_data/"
openfile_name="住所変更届_003.pdf"

#複数ファイルに対して
#指定パス内のファイルをリストで取得
openfile_list=os.listdir(openfile_path)

#pdfファイルを開く
#第一引数にパスに開くソフトの実行ファイル、第二引数に開くファイルのパス
# pdf_pro=subprocess.Popen([acr_path,openfile_path+openfile_name])
# time.sleep(3)

#閉じる操作
#マウスを右上に持っていきクリックさせる(あらかじめ右上の座標を調べる必要がある)
Close_button_x=1881
Close_button_y=10
# pag.click(Close_button_x,Close_button_y)

#画像認識で位置検出
def detect_name_pos():
    pag.moveTo(1,1)
    #PCの処理的な関係でうまくいかないこともあるので50回くらい試すのがおすすめ
    for count in range(50):
        try:
            x,y,w,h = pag.locateOnScreen("simei.PNG")
            break
        except ImageNotFoundException:
            time.sleep(1)
    return x,y,w,h

#pythonファイルが実行されたら真っ先に呼ばれるようにする
if __name__ == "__main__":
    for idx, file in enumerate(openfile_list):
        print("file : ",file)
        pdf_pro=subprocess.Popen([acr_path,openfile_path+file])
        time.sleep(1.5)

        #「氏名：」の位置を検出
        x,y,w,h=detect_name_pos()
        print(x,y,w,h)

        pag.click(Close_button_x,Close_button_y)
        time.sleep(1)

