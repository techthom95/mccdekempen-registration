#!/usr/bin/env python3
from win32com.client import Dispatch

def printjob(com):
    try:
        com.StartPrintJob()
        com.Print(1,False)
        com.EndPrintJob()
    except Exception as e:
        print("[+] DYMO ERROR,", e)


def main(var1, var2, var3, var4, var5):
    # Variables
    mylabel = "dymo.label"
    selectPrinter = "DYMO LabelWriter 450"

    try:
        labelcom = Dispatch("Dymo.DymoAddIn")
        labeltext = Dispatch("Dymo.DymoLabels")

        isOpen = labelcom.Open(mylabel)
        labelcom.SelectPrinter(selectPrinter)

        labeltext.SetField("TEXT1", var1)
        labeltext.SetField("TEXT2", var2)
        labeltext.SetField("TEXT3", var3)
        labeltext.SetField("TEXT4", var4)
        labeltext.SetField("TEXT5", var5)
    except Exception as e:
        print("[+] DYMO ERROR,", e)
    
    printjob(labelcom)