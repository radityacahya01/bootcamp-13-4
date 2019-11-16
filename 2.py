#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# File:       2.py
# Nama:       Raditya Cahya Pratama
# Tanggal:    16 November 2019
# Deskripsi:  Program untuk menjawab soal nomor 2 dari Seleksi Bootcamp Arkademy Batch 13-4
#             Menghitung jumlah kata dalam sebuah string


def login():
    import re
    while True:
        username=input("username:")
        if len(username)==7:
            for i in username:
                if re.search("[A-Z]", i):
                    pass
                else:
                    print(False)
                    break
            print(True)
        else:
            print(False)
        password=input("password:")
        if len(password)==7:
            if re.search("*", password).start()==3:
                pw=password.split('*')
                print(pw)
        break
    
login()

