#!/usr/bin/env python
# coding: utf-8

# In[2]:


# File:       1.py
# Nama:       Raditya Cahya Pratama
# Tanggal:    16 November 2019
# Deskripsi:  Program untuk menjawab soal nomor 1 dari Seleksi Bootcamp Arkademy Batch 13-4
#             Membuat fungsi untuk memenginformasikan biodata


# Import JSON library
import json

# Membuat fungsi biodata
def biodata(nama, umur):
    bio = {'name':nama,
           'age':umur, 
           'address':'Jl. Mesan No. 54, Blunyahgede, Sleman', 
           'hobbies':'Watch TV Series',
           'is_married':False,
           'list_school':{'name':'Universitas Gadjah Mada', 'year_in':2015, 'year_out':2019, 'major':'Engineering Physics'},
           'skills':{'skill_name':'Statistics and Programming', 'level':'Advanced'},
           'interest_in_coding':True
          }
    bio = json.dumps(bio)
    return bio

# Mencoba keluaran fungsi
print(biodata("Raditya Cahya Pratama", 22))

