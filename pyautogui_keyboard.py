import pyautogui as pag

#書き込み
#intervalは書き込みの間の時間
#writeの前に、書き込みしたい位置まで移動してクリックする動作が必要
# x,y=pag.position()
# print(x,y)
pag.moveTo(278,471)
pag.click()
# pag.write("こんにちは　PyAutoGUI",interval=0.25)

#pressでキーボードのボタンを押す動作
# pag.press("enter")
#回数が増えた問いは配列のように書く
# pag.press(['enter','enter'])
# pag.press('enter',presses=3,interval=0.25)

#押せるキーボードの種類を確認できる
# print(pag.KEYBOARD_KEYS)

#ショートカットキー
pag.hotkey("ctrl","shift","esc")