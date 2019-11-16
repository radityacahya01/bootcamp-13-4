#!/usr/bin/env python
# coding: utf-8

# In[1]:


# File:       3.py
# Nama:       Raditya Cahya Pratama
# Tanggal:    16 November 2019
# Deskripsi:  Program untuk menjawab soal nomor 3 dari Seleksi Bootcamp Arkademy Batch 13-4
#             Menghitung jumlah kata dalam sebuah string


def cek_kata(String):
    import re
    kalimat=(String.split())
    jumlah_kata_semua=len(kalimat)
    jumlah_kata=0
    for kata in kalimat:
        if kata=='1' or kata=='2' or kata=='3' or kata=='4' or kata=='5' or kata=='6' or kata=='7' or kata=='8' or kata=='9':
            pass
        else:
            jumlah_kata+=1
    proporsi=str(jumlah_kata)+'/'+str(jumlah_kata_semua)
    return(proporsi)
        
print(cek_kata("2 pasang sandal hilang"))

