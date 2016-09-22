# -*- coding: utf-8 -*-
#Pretvorik enot

print("Živjo, ta program pretvarja kilometre v milje.")

while True:
    kilometri = int(raw_input("Vnesi število kilometrov: "))
    milje = kilometri*1.609344
    print(str(kilometri)+" kilometrov je "+str(milje)+" milj.")
    vprasanje = str(raw_input("Ali želiš še eno pretvorbo? (da/ne)"))
    if vprasanje == "ne":
        print("Adijo!")
        break