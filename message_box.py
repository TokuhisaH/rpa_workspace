import pyautogui as pag

#アラートを出す
# pag.alert(text='Hello',title="alert bOX",button="OK")

#確認ボタン
# pag.confirm(text="HELLO?",title="confirm BOX",buttons=["OK","cancel"])

#テキスト入力ボックス
#defaultは事前に何か入れておきたい文字列
# text=pag.prompt(text='HEllo',title='TEXT BOX',default='',)
# print(text)

#password
#maskで入力文字を隠す
password=pag.password(text='HEllo',title='pass BOX',default='',mask="ち")
print(password)