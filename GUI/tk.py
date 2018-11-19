from tkinter import *
from PIL import Image
#from PIL import ImageTK

def swipeClick():
    novi = Toplevel()
    novi.title("Next Song Gesture: Swipe Right")
    canvas = Canvas(novi, width=500, height=500)
    canvas.pack(expand=YES, fill = BOTH)
    swipe = PhotoImage(file = "swipe.gif")
    canvas.create_image(50, 100, image = swipe, anchor = NW)
    canvas.swipe = swipe
	
def keyClick():
    novi = Toplevel()
    novi.title("Play/Pause Gesture: Key Press")
    canvas = Canvas(novi, width=500, height=500)
    canvas.pack(expand=YES, fill = BOTH)
    swipe = PhotoImage(file = "keyTap.gif")
    canvas.create_image(50, 100, image = swipe, anchor = NW)
    canvas.swipe = swipe
	
def screenClick():
    novi = Toplevel()
    novi.title("Mute/Unmute: Screen Tap")
    canvas = Canvas(novi, width=500, height=500)
    canvas.pack(expand=YES, fill = BOTH)
    swipe = PhotoImage(file = "screentap.gif")
    canvas.create_image(50, 100, image = swipe, anchor = NW)
    canvas.swipe = swipe
	
def swipeClickPrev():
    novi = Toplevel()
    novi.title("Previous Song Gesture: Swipe Left")
    canvas = Canvas(novi, width=500, height=500)
    canvas.pack(expand=YES, fill = BOTH)
    swipe = PhotoImage(file = "swipe.gif")
    canvas.create_image(50, 100, image = swipe, anchor = NW)
    canvas.swipe = swipe

window = Tk()
window.geometry("500x500")
window.title("M.I.G.I.")
lbl = Label(window, text = "Gesture Interaction Options", font = ("Arial Bold", 10))
nextSong = Button(window, text = "Next Song", command = swipeClick)
previous = Button(window, text = "Previous Song", command = swipeClickPrev)
play = Button(window, text = "Play/Pause", command = keyClick)
mute = Button(window, text = "Mute/Unmute", command = screenClick)

swipe = PhotoImage(file = "swipe.gif")
screen = PhotoImage(file = "screentap.gif")
key = PhotoImage(file = "keyTap.gif")
#key = key.resize((10, 10), Image.ANTIALIAS)
#swipe = swipe.resize((10, 10), Image.ANTIALIAS)
#screen = screen.resize((10, 10), Image.ANTIALIAS)
swipePic = Label(image = swipe)
#swipePic.pack()
screenTap = Label(image = screen)
keyTap = Label(image = key)

lbl.grid(column=0, row=0)
nextSong.grid(column = 0, row = 4)
#swipePic.grid(column = 2, row = 1)
previous.grid(column = 10, row = 4)
#swipePic.grid(column = 2, row= 2)
play.grid(column = 0, row = 12)
#keyTap.grid(column = 2, row = 3)
mute.grid(column = 10, row = 12)
#screenTap.grid(column = 2, row = 4)
window.mainloop()
