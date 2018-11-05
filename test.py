from pynput.keyboard import Key, Controller, Listener, KeyCode
import keyboard
import win32api
import Leap

class LeapEventListener(Leap.Listener):
    def on_connect(self, controller):
        print ("Connected")

controller = Leap.Controller()
listener = LeapEventListener
controller.add_listener(listener)
keyboard1 = Controller()
VK_ESCAPE = 0x1B
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
code = win32api.MapVirtualKey(VK_ESCAPE, 0)
code1 = win32api.MapVirtualKey(VK_MEDIA_PLAY_PAUSE, 0)
code2 = win32api.MapVirtualKey(VK_MEDIA_NEXT_TRACK, 0)
code3 = win32api.MapVirtualKey(VK_MEDIA_PREV_TRACK, 0)
#keyboard.is+pressed('esc')

def press(event):
    #if event.name == 'esc':
        #print('Escape pressed, exiting...')
        
    if event.name == 'n':
        win32api.keybd_event(VK_ESCAPE, code)
        
    elif event.name == 'z':
        win32api.keybd_event(VK_MEDIA_PLAY_PAUSE, code1)
        
    elif event.name == 'x':
        win32api.keybd_event(VK_MEDIA_PREV_TRACK, code3)
    
    elif event.name == 'c':
        win32api.keybd_event(VK_MEDIA_NEXT_TRACK, code2)

keyboard.on_press(press)

while True:
    if keyboard.is_pressed('esc'):
        print('ESC pressed, exiting...')
        break
        
