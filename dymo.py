#!/usr/bin/env python3
from os import path
from win32com.client import Dispatch

def main():
    curdir = path.dirname(path.abspath(__file__))
    mylabel = path.join(curdir,"my.label")
    selectPrinter = "DYMO LabelWriter 450"

    try:
        labelCom = Dispatch("Dymo.DymoAddIn")
        labelText = Dispatch("Dymo.DymoLabels")

        isOpen = labelCom.Open(mylabel)
        labelCom.SelectPrinter(selectPrinter)

        labelText.SetField("TEXT1", "Hoi")
        labelText.SetField("TEXT2", "Hoi2")

        labelCom.StartPrintJob()
        labelCom.Print(1,False)
        labelCom.EndPrintJob()
    except Exception as e:
        print("[+] DYMO ERROR,", e)