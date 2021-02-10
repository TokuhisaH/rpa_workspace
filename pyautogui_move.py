import pyautogui as pag

#指定した座標までカーソルが移動する
#3つ目の引数で移動までの時間を指定できる。何もないと0.1秒
#pag.moveTo(1000,500)

# m_posi_x,m_posi_y=pag.position()
# pag.moveTo(m_posi_x+100,m_posi_y+100,1)

#現在地からx,yにそれぞれプラス100　上の処理と同じ
pag.move(100,100,1)