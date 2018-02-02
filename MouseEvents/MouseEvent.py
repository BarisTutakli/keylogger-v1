from __future__ import print_function
from Logger import Logs
import datetime
instanTime=datetime.datetime.now()



def OnMouseEvent(self):
    self.time_details = "{}.{}.{} - {}:{}:{} ".format(instanTime.day, instanTime.month,
                                                                   instanTime.year,
                                                                   instanTime.hour, instanTime.minute,
                                                                   instanTime.second)
    self.MouseData = {
        "MessageName": self.MessageName,
        "MouseMessage": self.Message,
        "timeDetails": self.time_details,
        "Window": self.Window,
        "WindowName": self.WindowName,
        "MousePosition": self.Position,
        "Wheel": self.Wheel,
        "ınjected": self.Injected

    }
    Logs.Registre("data.txt",self.MouseData)

    return True