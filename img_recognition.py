import pyautogui as pag

#スクショ
#()内に保存したいファイル名を指定する
#regionで範囲を指定可能
# img=pag.screenshot("screenshot.png",region=(0,0,500,500))

#画像認識機能による物体検出
icon_loc=pag.locateOnScreen("icon.PNG")
print(icon_loc)