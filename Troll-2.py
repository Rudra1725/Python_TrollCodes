#Turns the main screen Black until user hit Alt+F4 to stop file he cant able to close it manually 
import tkinter 

r = tkinter.Tk()

r.attributes('-fullscreen', True)
r.attributes('-topmost', True)
r.config(bg='black')
r.protocol("WM_DELETE_WINDOW", lambda: None)
r.mainloop()
#End
