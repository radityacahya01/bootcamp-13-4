#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# File:       5.py
# Nama:       Raditya Cahya Pratama
# Tanggal:    16 November 2019
# Deskripsi:  Program untuk menjawab soal nomor 5 dari Seleksi Bootcamp Arkademy Batch 13-4
#             Membuat fungsi untuk memenginformasikan biodata

def createTriangle(angka):
    jumlah_spasi=angka
    for i in range(angka):
        print(' '*(jumlah_spasi-1) + '*'*(i+1))
        jumlah_spasi-=1

