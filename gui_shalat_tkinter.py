import urllib3
import json
import tkinter as tk
from tkinter import ttk
from tkinter import *
from datetime import datetime
from time import sleep, strftime

http = urllib3.PoolManager()
url = 'https://api.pray.zone/v2/times/today.json?city=medan&school=10'

win = tk.Tk()
tampil=""
win.title("Yuk Shalat")

imsak = ''
subuh = ''
terbit = ''
zuhur = ''
ashar = ''
terbenam = ''
magrib = ''
isya = ''
tengah_malam = ''

masehi = ''
hijriah = ''

sumber = ''
metode =''
ud_jam = ''

label_judul = ttk.Label(win, text="Jadwal Shalat Kota Medan Hari Ini",
                        font=("calibri", 40, 'bold'),
                        background = 'green',
                        foreground = 'white')
label_judul.grid(column=0, row=0, columnspan = 7)

footer = ttk.Label(win, font=("calibri", 12),
                   foreground = 'green')
footer.grid(column=0, row=4, columnspan = 7)

label_imsak = ttk.Label(win, text="Imsak", font=("calibri",20))
label_imsak.grid(column=0, row=2)
jw_imsak = ttk.Label(win, font=("calibri",20))
jw_imsak.grid(column=0, row=3)

label_subuh = ttk.Label(win, text="Subuh", font=("calibri",20))
label_subuh.grid(column=1, row=2)
jw_subuh = ttk.Label(win, font=("calibri",20))
jw_subuh.grid(column=1, row=3)

label_terbit = ttk.Label(win, text="Terbit", font=("calibri",20))
label_terbit.grid(column=2, row=2)
jw_terbit = ttk.Label(win, font=("calibri",20))
jw_terbit.grid(column=2, row=3)

label_zuhur = ttk.Label(win, text="Zuhur", font=("calibri",20))
label_zuhur.grid(column=3, row=2)
jw_zuhur = ttk.Label(win, font=("calibri",20))
jw_zuhur.grid(column=3, row=3)

label_ashar = ttk.Label(win, text="Ashar", font=("calibri",20))
label_ashar.grid(column=4, row=2)
jw_ashar = ttk.Label(win, font=("calibri",20))
jw_ashar.grid(column=4, row=3)

label_magrib = ttk.Label(win, text="Magrib", font=("calibri",20))
label_magrib.grid(column=5, row=2)
jw_magrib = ttk.Label(win, font=("calibri",20))
jw_magrib.grid(column=5, row=3)

label_isya = ttk.Label(win, text="Isya", font=("calibri",20))
label_isya.grid(column=6, row=2)
jw_isya = ttk.Label(win, font=("calibri",20))
jw_isya.grid(column=6, row=3)

"""
print("Jadwal Shalat Hari Ini, Subuh: "
  + subuh + ", Zhuhur: " + zuhur
  + ", Ashar: " + ashar + ", Maghrib: "
  + magrib + ", Isya: " + isya)
"""

def tick():
    r = http.request('GET', url)
    encode = json.loads(r.data)

    ud_jam = strftime("%H:%M")

    jadwal = encode['results']['datetime']
    hasil = encode['results']['settings']

    sumber = hasil['school']
    metode = hasil['juristic']

    for data in jadwal:
        imsak = data['times']['Imsak']
        subuh = data['times']['Fajr']
        terbit = data['times']['Sunrise']
        zuhur = data['times']['Dhuhr']
        ashar =  data['times']['Asr']
        terbenam = data['times']['Sunset']
        magrib = data['times']['Maghrib']
        isya  = data['times']['Isha']
        tengah_malam = data['times']['Midnight']

        masehi = data['date']['gregorian']
        hijriah = data['date']['hijri']

    jw_imsak.configure(text=imsak)
    jw_subuh.configure(text=subuh)
    jw_terbit.configure(text=terbit)
    jw_zuhur.configure(text=zuhur)
    jw_ashar.configure(text=ashar)
    jw_magrib.configure(text=magrib)
    jw_isya.configure(text=isya)

    if ud_jam == imsak:
        jw_imsak.configure(foreground = 'red')
    elif ud_jam == subuh:
        jw_subuh.configure(foreground = 'red')
    elif ud_jam == zuhur:
        jw_zuhur.configure(foreground = 'red')
    elif ud_jam == ashar:
        jw_ashar.configure(foreground = 'red')
    elif ud_jam == magrib:
        jw_magrib.configure(foreground = 'red')
    elif ud_jam == isya:
        jw_isya.configure(foreground = 'red') 

    
    footer.configure(text="Sumber: " + sumber + " - Metode: " + metode)
    
    label_jam.configure(text = "Tanggal: " + masehi + " M / "
                        + hijriah + " H - Jam: " + ud_jam)
    label_jam.after(1000, tick)

label_jam = ttk.Label(win,  font=("calibri", 20))
label_jam.grid(column=0, row=1, columnspan = 7)

tick()
win.mainloop()
