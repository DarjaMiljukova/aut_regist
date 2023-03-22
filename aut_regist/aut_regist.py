from random import*
import random
from string import*
import string
from tkinter import *
from tkinter import ttk
from ast import Lambda





#SUNKEN , RAISED , GROOVE         relief=GROOVE

#https://sites.google.com/view/paztronomer/blog/basic/python-colors
#https://docs.python.org/3/library/tkinter.font.html


kasutaja = {"juhataja": "parool"}

veebisait=Tk()
veebisait.geometry("600x600")
veebisait.title("Registreerimine ja autoriseerimine")





#меню
def func(i):
    tabs.select(i)




M=Menu(veebisait)
veebisait.config(menu=M)
m1=Menu(M)
M.add_cascade(label="Tabs", menu=m1)
m1.add_command(label="Registreerimine", accelerator="Command+R", command=lambda:func(0))
m1.add_command(label="Autoriseerimine", accelerator="Command+A", command=lambda:func(1))
m1.add_command(label="Saidi tugi", accelerator="Command+S", command=lambda:func(2))
m1.add_separator()




tabs=ttk.Notebook(veebisait)
text=["Registreerimine","Autoriseerimine","Saidi tugi"]

tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)



tabs.add(tab1, text=text[0])
tabs.add(tab2, text=text[1])
tabs.add(tab3, text=text[2])

tabs.pack(fill="both")




# регистрация
def registreemi():
    if not validate_input():
        return
    user = entry_kasutajanimi.get()
    passw = entry_passw.get()
    if user in kasutaja:
        lbl_status.config(text="Kasutajanimi on juba võetud")
    else:
        kasutaja[user] = passw
        lbl_status.config(text="Kasutaja registreerimine õnnestus")








# вход в систему
def log():
    if not validate_input():
        return
    user = entry_kasutajanimi.get()
    passw = entry_passw.get()
    if user not in kasutaja:
        lbl_status.config(text="Kasutajanime ei leitud")
    elif kasutaja[user] != passw:
        lbl_status.config(text="Vale salasõna")
    else:
        lbl_status.config(text="Sisselogimine õnnestus")



# смена пароля
def cha_pass():
    kasutajad = entry_kasutajanimi.get()
    old_passw = entry_passw.get()
    new_passw = entry_passw.get()

    if kasutajad not in kasutaja:
        lbl_status.config(text="Kasutajanime ei leitud")
    elif kasutaja[kasutajad] != old_passw:
        lbl_status.config(text="Vale salasõna")
    else:
        kasutaja[kasutajad] = new_passw
        lbl_status.config(text="Salasõna muutmine õnnestus")



# ошибки при вводе пароля
def validate_input():
    user = entry_kasutajanimi.get()
    passw = entry_passw.get()
    if not user:
        lbl_status.config(text="Kasutajanimi ei tohi olla tühi")
        return False
    elif not passw:
        lbl_status.config(text="Parool ei tohi olla tühi")
        return False
    elif len(passw) < 8:
        lbl_status.config(text="Parool peab olema vähemalt 8 tähemärki pikk")
        return False
    elif not any(c.isupper() for c in passw):
        lbl_status.config(text="Parool peab sisaldama vähemalt ühte suurtähte")
        return False
    elif not any(c.islower() for c in passw):
        lbl_status.config(text="Parool peab sisaldama vähemalt ühte väiketähte")
        return False
    elif not any(c.isdigit() for c in passw):
        lbl_status.config(text="Parool peab sisaldama vähemalt ühte numbrit")
        return False
    elif not any(c in string.punctuation for c in passw):
        lbl_status.config(text="Parool peab sisaldama vähemalt ühte erimärki")
        return False
    else:
        lbl_status.config(text="")
        return True




# создание пароля
def gen_pass():
    while True:
        length = 12
        chars = string.ascii_letters + string.digits + string.punctuation
        parool = "".join(random.choice(chars) for _ in range(length))
        if (any(char.isupper() for char in parool) and
            any(char.islower() for char in parool) and
            any(char.isdigit() for char in parool) and
            any(char in string.punctuation for char in parool)):
            entry_passw.delete(0, END)
            entry_passw.insert(0, parool)
            break




# восстановление пароля
def rec_pass():
    user = entry_kasutajanimi.get()
    if user not in kasutaja:
        lbl_status.config(text="Kasutajanime ei leitud")
    else:
        parool = kasutaja[user]
        lbl_status.config(text=f"Sinu parool on {parool}")





# смена пароля
def cha_pass():

    if not validate_input():
        return
    user = entry_kasutajanimi.get()
    passw = entry_passw.get()
    if user not in kasutaja:
        lbl_status.config(text="Kasutajanime ei leitud")
    else:
        kasutaja[user] = passw
        lbl_status.config(text="Salasõna muutmine õnnestus")










lbl_kasutajanimi = Label(veebisait, text="Sinu kasutajanimi: ", font="Courier 20", bg="mediumslateblue")
lbl_kasutajanimi.pack(pady=8)        #отступ
entry_kasutajanimi = Entry(veebisait, font="Courier 20", bg="slategrey", fg="darkslateblue")
entry_kasutajanimi.pack()



#parool
lbl_pass = Label(veebisait, text="Sinu salasõna: ", font="Courier 20", bg="mediumslateblue")
lbl_pass.pack(pady=8)
entry_passw = Entry(veebisait, show="*", font="Courier 20", bg="slategrey", fg="darkslateblue")
entry_passw.pack()



#registr
rad_reg = Radiobutton(veebisait, text="Registreerimine", command=registreemi, font="Courier 20", bg="mediumslateblue", relief=GROOVE, value=1)
rad_reg.pack(pady=10) 





#login
rad_login = Radiobutton(veebisait, text="Logi sisse", command=log, font="Courier 20", bg="mediumslateblue", value=2)
rad_login.pack()





lbl_status = Label(veebisait, text="", font="Courier 20", bg="mediumslateblue")
lbl_status.pack(pady=10)




#generatsion
btn_generate = Button(veebisait, text="Parooli loomine", command=gen_pass, font="Courier 20", bg="mediumslateblue", relief=GROOVE)
btn_generate.pack(pady=10)



#kustutama
btn_recover = Button(veebisait, text="Parooli taastamine", command=rec_pass, font="Courier 20", bg="mediumslateblue", relief=GROOVE)
btn_recover.pack(pady=10)


#muuda
btn_change = Button(veebisait, text="Muuda salasõna", command=cha_pass, font="Courier 20", bg="mediumslateblue", relief=GROOVE)
btn_change.pack(pady=10)




veebisait.config(bg="midnightblue")
veebisait.mainloop() 
