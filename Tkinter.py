import tkinter
print(tkinter.TclVersion)
print(tkinter.TkVersion)

tkinter._test()

mainWindow= tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("640x480")
mainWindow.mainloop()
