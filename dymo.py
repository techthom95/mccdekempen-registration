#!/usr/bin/env python3
# dymo.py>
from configparser import *
from win32com.client import Dispatch

# Define configuration
def config():
    try:
        config = ConfigParser()
        config.read("config.ini")
        var1 = config.get("DYMO", "label")
        var2 = config.get("DYMO", "printer")
        return var1, var2
    except Exception as e:
        print("[+] DYMO ERROR,", e)
        return -1

# Define print job
def printjob(com):
    try:
        com.StartPrintJob()
        com.Print(1,False)
        com.EndPrintJob()
        print("[+] DYMO INFO, label printed")
    except Exception as e:
        print("[+] DYMO ERROR,", e)
        return -1

# Define main function
def main(**var):
    # Read configuration
    mylabel = config()[0]
    selectPrinter = config()[0]
    if mylabel == -1 or selectPrinter == -1:
        return -1

    try:
        print("[+] DYMO INFO, preparing label")
        labelcom = Dispatch("Dymo.DymoAddIn")
        labeltext = Dispatch("Dymo.DymoLabels")

        isOpen = labelcom.Open(mylabel)
        labelcom.SelectPrinter(selectPrinter)

        labeltext.SetField("TEXT1", var.get("firstname"))
        labeltext.SetField("TEXT2", var.get("insertion"))
        labeltext.SetField("TEXT3", var.get("lastname"))
        labeltext.SetField("TEXT4", var.get("place"))
        labeltext.SetField("TEXT5", var.get("date-of-birth"))
    except Exception as e:
        print("[+] DYMO ERROR,", e)
        return -1
    
    if printjob(labelcom) == -1:
        return -1
    
# DEBUG TEST
if __name__ == "__main__":
    list = { "firstname":"test-fname",
                "insertion":"test-insert",
                "lastname":"test-lname",
                "place":"test-place",
                "date-of-birth":"test-date"
                }
    main(**list)