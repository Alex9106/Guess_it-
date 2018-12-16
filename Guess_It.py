from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', "Gaseste username-ul si parola !")
tkinter.messagebox.showinfo( "Window Title", "Username-ul poate fi format din: 'nick' sau 'norman'."
                            "Parola din: cifrele 0, 1 si 2 si literele 'a' si 'b'."
                            "Gasiti username-ul potrivit si parola potrivita pentru a debloca, contul. \n Succes!!! ")

label_1 = Label(root, text='Username')
label_2 = Label(root, text='Password')
label_3 = Label(root)
entry_1 = Entry(root)
entry_2 = Entry(root)
entry_3 = Entry(root)


label_1.grid(row=0)
label_2.grid(row=1)
label_3.grid(row=3, column=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
entry_3.grid(row=2, column=1)

def answer():

    number_1 = Entry.get(entry_1)
    number_2 = Entry.get(entry_2)


    if number_1 == "nick" and number_2 == "120ba":
        value = "--Felicitari!--"
    elif number_1 == "nick" or number_2 == "120ba":
        value = "--Ai nimerit una. Inca putin!--"
    else:
        value = "--Nu dispera. Mai incearca! :)--"
        
    Entry.insert(entry_3, 0 , value)


button = Button(label_3, text="Check", fg="red", command=answer)
button.pack()

root.mainloop()
