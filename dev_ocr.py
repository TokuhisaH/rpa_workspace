from PIL import Image
import sys
import pyocr


#※注意
#C:\Users\***\anaconda3\envs\****\Lib\site-packages\pyocr内の
#tesseract.pyとbuilder.pyの-psmを--psmに修正する必要がある


#pyocrから使えるツールを拾ってくる。ここだとtesseract
tools = pyocr.get_available_tools()

#ツールが見つからなかった場合の処理
if len(tools)==0:
    print("OCRツールが見つかりませんでした")
    sys.exit(1)

#
tool=tools[0]
print("use tool : ",tool.get_name())

#使える言語取得
#事前にgithubのtessdocのdata-filesからjapaneseを持ってきて
#C:\Users\***\Anaconda3\envs\***\Library\bin\tessdataフォルダへ
langs = tool.get_available_languages()
print(langs)


#画像から文字を認識するメソッド
#第二引数で認識文字列を指定
txt = tool.image_to_string(Image.open("test.png"),lang="jpn")
#空白を消す処理
txt=txt.replace(" ","")
print(txt)


