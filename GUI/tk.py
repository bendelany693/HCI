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
spc = Label(window, text = " ")
lbl2 = Label(window, text = "M.I.G.I.: Music Interaction and Gesture Identification", font = ("Arial Bold", 10), anchor = "w")
desc = Label(window, text = "MIGI uses Leap motion gesture identification and the Windows API to ", anchor = "w")
desc2 = Label(window, text = "give users an easy, intuitive way to interact with their media player.", anchor = "w") 
lbl1 = Label(window, text = "Gesture Interaction Options", font = ("Arial Bold", 10), anchor = "w")
nextSong = Button(window, text = "Next Song", command = swipeClick, anchor = "w")
previous = Button(window, text = "Previous Song", command = swipeClickPrev, anchor = "w")
play = Button(window, text = "Play/Pause", command = keyClick, anchor = "w")
mute = Button(window, text = "Mute/Unmute", command = screenClick, anchor = "w")

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

lbl2.grid(column=0, row=0)
desc.grid(column=0, row=1)
desc2.grid(column=0, row=2)
spc.grid(column = 0, row = 3)
spc.grid(column = 0, row = 4)
spc.grid(column = 0, row = 5)

lbl1.grid(column=0, row=5)
nextSong.grid(column = 0, row = 6)
#swipePic.grid(column = 2, row = 1)
previous.grid(column = 0, row = 7)
#swipePic.grid(column = 2, row= 2)
play.grid(column = 0, row = 8)
#keyTap.grid(column = 2, row = 3)
mute.grid(column = 0, row = 9)
#screenTap.grid(column = 2, row = 4)
window.mainloop()
