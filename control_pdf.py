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

#氏名の幅を調べる
def get_name_width(x,w):
    #氏名の座標が終わる位置（事前に調べておく）
    end_x = 1066
    #このstart_xは「氏名：」の開始位置なので幅のwを足せば名前の開始位置になる
    start_x=x+w
    NAME_W = end_x -start_x
    return NAME_W

def get_name_image(x,y,w,h,NAME_W):
    start_x=x+w
    start_y=y
    name_img=pag.screenshot("name_img.png",region=(start_x,start_y,NAME_W,h))
    return name_img

#OCRを動かすメソッド
def run_ocr(tool,name_img):
    result = tool.image_to_string(name_img,lang='jpn')
    result = result.replace(" ","")
    print(result)
    return result

#スプレッドシート等に名前を記述するメソッド
def copy_name_data(name_list):
    #記入するスプレッドシートのセルの位置
    pag.moveTo(94,447)
    pag.click()

    for name in name_list:
        #日本語入力するためにpyperclipでcopyし、hotkeyで貼り付け
        pyperclip.copy(name)
        pag.hotkey("ctrl","v")
        pag.press("enter")
        pag.press("enter")


#pythonファイルがコマンドラインから実行されたら呼ばれるようにする
if __name__ == "__main__":
    tools = pyocr.get_available_tools()
    if len(tools)==0:
        print("No OCR Tool found")
        sys.exit(1)
    tool = tools[0]

    #抽出した名前を保存するリスト
    name_list=[]

    #経過時間を図る変数（pdf_pro.poll()で使う）
    WAIT_TIME=5


    for idx, file in enumerate(openfile_list):
        #前のPDFが閉じられているか確認する処理
        if idx !=0:
            #time.time()で現在時刻を取得できる
            start = time.time()
            elapsed_time = 0
            #.poll()は前のプロセスが終了していない場合はNoneを返す
            while pdf_pro.poll()== None:
                elapsed_time = time.time() - start
                if elapsed_time > WAIT_TIME:
                    print("STOP PROCESS")
                    sys.exit(1)
        
        print("file : ",file)
        pdf_pro=subprocess.Popen([acr_path,openfile_path+file])
        time.sleep(1)

        #「氏名：」の位置を検出
        x,y,w,h=detect_name_pos()
        #print(x,y,w,h)

        #名前の横幅
        NAME_W = get_name_width(x,w)

        #名前の画像取得
        name_img = get_name_image(x,y,w,h,NAME_W)

        #名前の画像から文字列を取得
        result=(run_ocr(tool,name_img))
        name_list.append(result)

        pag.click(Close_button_x,Close_button_y)
        time.sleep(1)

        # if idx == 3:
        #     break
    
    copy_name_data(name_list)

    pag.alert("無事に終わりました")

