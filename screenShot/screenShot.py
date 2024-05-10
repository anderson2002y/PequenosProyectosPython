from tkinter import*

win = Tk()
win.title("LoopGlitch Screenshoter")

def callback():
    mySS = pyautogui.screenshot()
    mySS.save(r'C:\screenShot\screen.jpg')  # RUTA PARA GUARDAR LA CAPTURA DE LA PANTALLA nombre.png or jpg'

button = Button(win, text = "Screenshot This !", command = callback)
button.grid(row = 50, column = 50)

win.mainloop()