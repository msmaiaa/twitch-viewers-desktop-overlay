import tkinter, win32api, win32con, pywintypes, time, requests

canal = str(input("Type the channel nickname: "))
tamanhoFonte = int(input("Font size: (recommended = 12 to 20)"))
qtd = int(input("Check every how many seconds?"))
qtd *= 1000
def reques():
    req = requests.get(f"https://decapi.me/twitch/viewercount/{canal}")
    res = req.content.decode()
    print(res + " viewers")
    return res

def overlay():
    label = tkinter.Label(text="", font=('Times New Roman',f'{tamanhoFonte}'), fg='red', bg='white')
    label.master.overrideredirect(True)
    
    #change the text position (x and y)
    label.master.geometry("+1875+0")
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")

    def on_after():
        res = reques()
        label.configure(text = f"{res}")
        label.after(qtd, on_after)
    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    label.pack()
    on_after()
    label.mainloop()

overlay()