from __future__ import print_function
from MouseEvents import MouseEvent
from KeyboardEvents import KeyboardEvent
import pyHook









hm = pyHook.HookManager()

hm.MouseAllButtonsDown = MouseEvent.OnMouseEvent
hm.KeyDown = KeyboardEvent.OnKeyboardEvent
hm.KeyDown = KeyboardEvent.OnKeyboardEvent


hm.HookMouse()
hm.HookKeyboard()

if __name__ == '__main__':
    import pythoncom

    pythoncom.PumpMessages()