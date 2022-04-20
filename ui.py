#!/usr/bin/env python3
from tkinter import *
from tkinter import font
from tkinter import messagebox
import sql, dymo

root=Tk() # Create main window
root.title('MCC De Kempen') # Window title
root.configure(bg='white') # Window background
#root.minsize(1200, 700) # Window size minimum
#root.state('zoomed') # Normal fullscreen
#root.attributes("-fullscreen", True) # Canvas fullscreen
icon=PhotoImage(file="image/icon.png") # Define icon
flag_nl=PhotoImage(file="image/nl.png").subsample(2,2) # Define NL flag
flag_en=PhotoImage(file="image/en.png").subsample(2,2) # Define EN flag
flag_de=PhotoImage(file="image/de.png").subsample(2,2) # Define DE flag
flag_es=PhotoImage(file="image/es.png").subsample(2,2) # Define ES flag
logo=PhotoImage(file="image/logo.png").zoom(3,2) # Define logo
root.iconphoto(True, icon) # Call icon
f1=font.Font(weight="bold", size=14) # Font 1
f2=font.Font(weight="bold", size=12) # Font 2

# Define languages
lang=[["Afdrukken", "Terug", "Voornaam", "Tussenvoegsel", "Achternaam", "Adres", "Postcode", "Nationaliteit", "Plaats", "Gebr. Datum", "E-Mail"],                                       #NL
        ["Print", "Back", "Firstname", "Insertion", "Lastname", "Address", "Zip Code", "Nationality", "Place", "Date of Birth", "E-Mail"],                                              #EN
        ["Drucken", "Zurück", "Vorname", "Einfügung", "Familiename", "Adresse", "Postleitzahl", "Nationalität", "Ort", "Geburtsdatum", "E-Mail"],                                       #DE
        ["Imprimir", "Volver", "Nombre de pila", "Inserción", "Nombre de familia", "Dirección de calle", "Código postal", "Nacionalidad", "Ciudad", "Fecha de cumpleaños", "E-mail"]]   #ES
langerr=[["Vul alle rode velden in!", "Database fout", "Printer werkt niet"],                           #NL
        ["Fill in all red fields!", "Database failure", "Printer not working"],                         #EN
        ["Füllen Sie alle roten Felder aus!", "Datenbankfehler", "Drucker funktioniert nicht"],         #DE
        ["Complete todos los campos rojos!", "Falla de la base de datos", "Impresora no funciona"]]     #ES
langinf=[["Neem label uit de printer"],             #NL
        ["Take label out of printer"],              #EN
        ["Nehmen Sie das Etikett aus dem Drucker"], #DE
        ["Sacar la etiqueta de la impresora"]]      #ES

# Function secondary window
def set_lang(langact):
    subroot=Toplevel(root) # Secondary window
    #subroot.attributes("-fullscreen", True) # Canvas fullscreen

    # Function Submit
    def submit():
        var = prepare()
        if var[0] != "" and var[2] != "" and var[3] != "" and var[4] != "" and var[5] != "" and var[6] != "" and var[7] != "" and var[8] != "":
            if dymo.main(var[0], var[1], var[2], var[7], var[8]) == -1:
                messagebox.showerror("ERROR", langerr[langact][2], parent=subroot)
            else:
                if sql.main(var[2], var[1], var[0], var[3], var[4], var[5], var[6], var[7], var[8]) == -1:
                    messagebox.showerror("ERROR", langerr[langact][1], parent=subroot)
                else:
                    clear()
                    messagebox.showinfo("INFO", langinf[langact][0], parent=subroot)
        else:
            messagebox.showerror("ERROR", langerr[langact][0], parent=subroot)

    # Function fill variables
    def prepare():
        var1 = textbox1.get()   # Firstname
        var2 = textbox2.get()   # Insertion
        var3 = textbox3.get()   # Lastname
        var4 = textbox4.get()   # Address
        var5 = textbox5.get()   # Zip Code
        var6 = textbox6.get()   # Nationality
        var7 = textbox7.get()   # Place
        var8 = textbox8.get()   # Date of Birth
        var9 = textbox9.get()   # E-Mail
        return var1, var2, var3, var4, var5, var6, var7, var8, var9

    # Function clear textboxes
    def clear():
        textbox1.delete(0, END)
        textbox2.delete(0, END)
        textbox3.delete(0, END)
        textbox4.delete(0, END)
        textbox5.delete(0, END)
        textbox6.delete(0, END)
        textbox7.delete(0, END)
        textbox8.delete(0, END)
        textbox9.delete(0, END)

    # Define sub window
    image = Label(subroot, image=logo)
    mainframe = Frame(subroot, bg="white")
    btn_submit = Button(subroot, text=lang[langact][0], height=2, bg="orange", font=f1, command=submit)
    btn_back = Button(subroot, text=lang[langact][1], height=2, bg="orange", font=f1, command=subroot.destroy)

    # Define "main frame" objects
    framerow0 = Frame(mainframe, bg="white")
    framerow1 = Frame(mainframe, bg="white")
    framerow2 = Frame(mainframe, bg="white")
    framerow3 = Frame(mainframe, bg="white")
    framerow4 = Frame(mainframe, bg="white")
    framerow5 = Frame(mainframe, bg="white")

    # Define "frame row 1" objects
    framerow1kl1 = Frame(framerow1, bg="white")
    framerow1kl2 = Frame(framerow1, bg="white")
    framerow1kl3 = Frame(framerow1, bg="white")
    label1 = Label(framerow1kl1, text=lang[langact][2], bg="white", width=12, font=f2)
    label2 = Label(framerow1kl2, text=lang[langact][3], bg="white", width=12, font=f2)
    label3 = Label(framerow1kl3, text=lang[langact][4], bg="white", width=12, font=f2)
    textbox1 = Entry(framerow1kl1, relief="solid", font=f2)
    textbox2 = Entry(framerow1kl2, relief="solid", font=f2)
    textbox3 = Entry(framerow1kl3, relief="solid", font=f2)

    # Define "frame row 2" objects
    framerow2kl1 = Frame(framerow2, bg="white")
    framerow2kl2 = Frame(framerow2, bg="white")
    label4 = Label(framerow2kl1, text=lang[langact][5], bg="white", width=12, font=f2)
    label5 = Label(framerow2kl2, text=lang[langact][6], bg="white", width=12, font=f2)
    textbox4 = Entry(framerow2kl1, relief="solid", font=f2)
    textbox5 = Entry(framerow2kl2, relief="solid", font=f2)

    # Define "frame row 3" objects
    framerow3kl1 = Frame(framerow3, bg="white")
    framerow3kl2 = Frame(framerow3, bg="white")
    label6 = Label(framerow3kl1, text=lang[langact][7], bg="white", width=12, font=f2)
    label7 = Label(framerow3kl2, text=lang[langact][8], bg="white", width=12, font=f2)
    textbox6 = Entry(framerow3kl1, relief="solid", font=f2)
    textbox7 = Entry(framerow3kl2, relief="solid", font=f2)

    # Define "frame row 4" objects
    framerow4kl1 = Frame(framerow4, bg="white")
    framerow4kl2 = Frame(framerow4, bg="white")
    label8 = Label(framerow4kl1, text=lang[langact][9], bg="white", width=12, font=f2)
    label9 = Label(framerow4kl2, text=lang[langact][10], bg="white", width=12, font=f2)
    textbox8 = Entry(framerow4kl1, relief="solid", font=f2)
    textbox9 = Entry(framerow4kl2, relief="solid", font=f2)

    # Place root objects in order
    image.pack(side=TOP)
    mainframe.pack(fill="both", expand="yes")
    btn_submit.pack(fill="both", pady=5, padx=20)
    btn_back.pack(fill="both", pady=5, padx=20)

    # Place "main frame" objects in order
    framerow0.pack(fill="both", expand="yes", pady=20)
    framerow1.pack(fill="both", expand="yes", pady=5, padx=20)
    framerow2.pack(fill="both", expand="yes", pady=5, padx=20)
    framerow3.pack(fill="both", expand="yes", pady=5, padx=20)
    framerow4.pack(fill="both", expand="yes", pady=5, padx=20)
    framerow5.pack(fill="both", expand="yes", pady=20)

    # Place "frame row 1" objects in order
    framerow1kl1.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    framerow1kl2.pack(side=LEFT, fill="both", expand="no", pady=5, padx=20)
    framerow1kl3.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    label1.pack(side=LEFT)
    textbox1.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)
    label2.pack(side=LEFT)
    textbox2.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)
    label3.pack(side=LEFT)
    textbox3.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)

    # Place "frame row 2" objects in order
    framerow2kl1.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    framerow2kl2.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    label4.pack(side=LEFT)
    textbox4.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)
    label5.pack(side=LEFT)
    textbox5.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)

    # Place "frame row 3" objects in order
    framerow3kl1.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    framerow3kl2.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    label6.pack(side=LEFT)
    textbox6.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)
    label7.pack(side=LEFT)
    textbox7.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)

    # Place "frame row 4" objects in order
    framerow4kl1.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    framerow4kl2.pack(side=LEFT, fill="both", expand="yes", pady=5, padx=20)
    label8.pack(side=LEFT)
    textbox8.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)
    label9.pack(side=LEFT)
    textbox9.pack(side=RIGHT, fill="x", expand="yes", ipady=8, padx=20)

# Define root window
mframerow0 = Frame(root, bg="white")
mframerow1 = Frame(root, bg="white")
mframerow0kl1 = Frame(mframerow0, bg="white")
mframerow0kl2 = Frame(mframerow0, bg="white")
mframerow1kl1 = Frame(mframerow1, bg="white")
mframerow1kl2 = Frame(mframerow1, bg="white")

# Define root objects
btn_nl = Button(mframerow0kl1, image=flag_nl, bg="white", command=lambda: set_lang(0))
btn_en = Button(mframerow0kl2, image=flag_en, bg="white", command=lambda: set_lang(1))
btn_de = Button(mframerow1kl1, image=flag_de, bg="white", command=lambda: set_lang(2))
btn_es = Button(mframerow1kl2, image=flag_es, bg="white", command=lambda: set_lang(3))

# Place root objects
mframerow0.pack(fill="both", expand="yes")
mframerow1.pack(fill="both", expand="yes")
mframerow0kl1.pack(side=LEFT, fill="both", expand="yes")
mframerow0kl2.pack(side=LEFT, fill="both", expand="yes")
mframerow1kl1.pack(side=LEFT, fill="both", expand="yes")
mframerow1kl2.pack(side=LEFT, fill="both", expand="yes")
btn_nl.pack(fill="both", expand="yes")
btn_en.pack(fill="both", expand="yes")
btn_de.pack(fill="both", expand="yes")
btn_es.pack(fill="both", expand="yes")

mainloop() # Running mainloop always last