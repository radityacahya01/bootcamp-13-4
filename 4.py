#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# File:       4.py
# Nama:       Raditya Cahya Pratama
# Tanggal:    16 November 2019
# Deskripsi:  Program untuk menjawab soal nomor 4 dari Seleksi Bootcamp Arkademy Batch 13-4
#             Membuat fungsi untuk memenginformasikan biodata

def findPair(s):
    if isinstance(s, list):
        s.sort()
        pair=0
        while len(s)>0:
            jumlah=s.count(s[0])
            del s[0:jumlah]
            pair+=jumlah//2
        if pair==0:
            return "Tidak ada pasangan yang ditemukan!"
        return str(pair) +" pasang"
    else:
        print("Bukan array")

