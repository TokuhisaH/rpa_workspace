import pyautogui as pag

#指定した座標までカーソルが移動する
#3つ目の引数で移動までの時間を指定できる。何もないと0.1秒
#pag.moveTo(1000,500)

# m_posi_x,m_posi_y=pag.position()
# pag.moveTo(m_posi_x+100,m_posi_y+100,1)

#現在地からx,yにそれぞれプラス100　上の処理と同じ
# pag.move(100,100,1)

#ドラッグ移動
# m_posi_x,m_posi_y=pag.position()
# pag.dragTo(m_posi_x+100,m_posi_y+100,1)

# pag.drag(100,100,1)

#クリック操作
#button引数でどっちをクリックするか
# pag.click(button='right')
#インターバル0.2秒で2回クリック
# pag.click(clicks=2, interval=0.2)
#下記でも同じことが可能
# pag.doubleClick()

# pag.click(button="right",clicks=3,interval=0.2)

#マウスを挙げた時と下した時で動作を分ける
# pag.mouseDown()
# pag.mouseUP()
# pag.mouseDown(); pag.mouseUP()

#スクロール
#第２，３引数に座標を指定することもできる
pag.scroll(-1000)