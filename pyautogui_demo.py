import pyautogui as pag
from time import sleep

#画面のサイズ取得、原点は左上
#print("画面サイズ",pag.size())

#scr_w,scr_h=pag.size()

#print(scr_w,scr_h)

#画面中央
#cent_x = scr_w/2
#cent_y = scr_h/2

#print("画面の中心の座標",cent_x,cent_y)

#マウスカーソルの位置
#print("マウスカーソルの位置",pag.position())

#m_posi_x,m_posi_y = pag.position()
#print("現在のマウス位置 x:",m_posi_x,"y:",m_posi_y)

try:
    while True:
        m_posi_x,m_posi_y = pag.position()
        print("現在のマウス位置 x:",m_posi_x,"y:",m_posi_y)
        sleep(1)
except KeyboardInterrupt:
    print("\n")