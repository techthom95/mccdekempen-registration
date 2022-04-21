#!/usr/bin/env python3
# dymo.py>
from configparser import *
from win32com.client import Dispatch

# Define configuration
def config():
    try:
        config = ConfigParser()
        config.read("config.ini")
        var1 = config["DYMO"]["label"]
        var2 = config["DYMO"]["printer"]
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
def main(var1, var2, var3, var4, var5):
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

        labeltext.SetField("TEXT1", var1)   # Firstname
        labeltext.SetField("TEXT2", var2)   # Insertion
        labeltext.SetField("TEXT3", var3)   # Lastname
        labeltext.SetField("TEXT4", var4)   # Place
        labeltext.SetField("TEXT5", var5)   # Date of Birth
    except Exception as e:
        print("[+] DYMO ERROR,", e)
        return -1
    
    if printjob(labelcom) == -1:
        return -1