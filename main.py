from tkinter import *

import tkintermapview

users:list = [    {"name":"lukasz","surname": "xxx","location":"opoczno","posts": 89 },]



def add_useer():
    imie = entry_name.get()
    nazwisko = entry_surname.get()
    posty = entry_posts.get()
    miejscowosc = entry_location.get()
    users.append( {"name": imie,
                   "surnamne": nazwisko,
                    "location":miejscowosc,
                    "posts": posty,
                   })
    print(users)
    entry_name.delete(0, END)
    entry_posts.delete(0, END)
    entry_surname.delete(0, END)
    entry_location.delete(0, END)
    entry_name.focus()
    show_users()

def show_users():
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(users):
        listbox_lista_obiektow.insert(idx, f"{idx+1}. {user["name"]} {user["surname"]} {user["location"]} {user["posts"]}")



 def delete_user():
    idx=listbox_lista_obiektow.index(ACTIVE)
    users.pop(idx)
    show_users()

def user_details():
    idx=listbox_lista_obiektow.index(ACTIVE)
    label_name_szczegoly_obiektu_wartosc.configure(text=users[idx]["name"])
    label_surname_szczegoly_obiektu_wartosc.configure(text=users[idx]["surname"])
    label_location_szczegoly_obiektu_wartosc.configure(text=users[idx]["location"])
    label_posts_szczegoly_obiektu_wartosc.configure(text=users[idx]["posts"])

    def edit_user():
        idx=listbox_lista_obiektow.index(ACTIVE)
        entry_name.insert(idx, users[idx]["name"])













root = Tk()
root.title("Mapbook_lw")
root.geometry("1024x768")


#RAMKI
ramka_lista_obiektów=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektow=Frame(root)
ramka_mapa=Frame(root)

ramka_lista_obiektów.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0)
ramka_mapa.grid(row=2, column=0, columnspan=2)


#RAMKA LISTA OBIEKTOW
label_lista_obiektow=Label(ramka_lista_obiektów,text="Lista obiektów")
label_lista_obiektow.grid(row=0, column=0, columnspan=3)
listbox_lista_obiektow=Listbox(ramka_lista_obiektów)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)
button_pokaz_szczegoly=Button(ramka_szczegoly_obiektow, text="Pokaż szczegóły", command=user_details)
button_pokaz_szczegoly.grid(row=2, column=0)
button_edytuj_obiekt=Button(ramka_szczegoly_obiektow, text="Edytuj obiekt")
button_edytuj_obiekt.grid(row=2, column=1)
button_usun_obiekt=Button(ramka_lista_obiektów, text="Usuń obiekt", command=delete_user)
button_usun_obiekt.grid(row=2, column=2)


#RAMKA FORMULARZ
label_formularz=Label(ramka_formularz, text="Formularz: ")
label_formularz.grid(row=0, column=0, columnspan=2)
label_name=Label(ramka_formularz, text="Imię: ")
label_name.grid(row=1, column=0, sticky=W)
label_surname=Label(ramka_formularz, text="Nazwisko: ")
label_surname.grid(row=2, column=0, sticky=W)
label_posts= Label(ramka_formularz, text="Liczba postów: ")
label_posts.grid(row=3, column=0, sticky=W)
label_location=Label(ramka_formularz, text="Miejscowość: ")
label_location.grid(row=4, column=0,sticky=W)

entry_name= Entry(ramka_formularz)
entry_name.grid(row=1, column=1,)
entry_surname=Entry(ramka_formularz)
entry_surname.grid(row=2, column=1)
entry_posts=Entry(ramka_formularz)
entry_posts.grid(row=3, column=1)
entry_location= Entry(ramka_formularz)
entry_location.grid(row=4, column=1)

button_dodaj_obiekt=Button(ramka_formularz, text="Dodaj", command=add_useer)
button_dodaj_obiekt.grid(row=5, column=1, columnspan=2)



#RAMKA SZCZEGÓŁY OBIEKTU
label_szczegoly_obiektu=Label(ramka_szczegoly_obiektow, text="Szczegoly użytkownika: ")
label_szczegoly_obiektu.grid(row=0, column=0, sticky=W)

label_name_szczegoly_obiektu= Label(ramka_szczegoly_obiektow, text="Imię: ")
label_name_szczegoly_obiektu.grid(row=1, column=0)

label_name_szczegoly_obiektu_wartosc= Label(ramka_szczegoly_obiektow, text="...")
label_name_szczegoly_obiektu_wartosc.grid(row=2, column=1)

# RAMKA MAPA
map_vidget=tkintermapview.TkinterMapView(ramka_mapa, width=1024, height= 400)
map_vidget.set_position(52.23, 21)
map_vidget.grid(row=0, column=0, columnspan=8)

root.mainloop()




