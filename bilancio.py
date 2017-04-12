#!/data/data/com.termux/files/usr/bin/python

from time import localtime, strftime
from os.path import expanduser, join
from pprint import pprint
from decimal import *

def file_output():
    home = expanduser('~')
    out_file_name = 'movimenti.dat'
    out_file = join(home, 'dati', out_file_name)
    return out_file

def carica_file(f):
    dati = []
    with open(f, "r") as df:
        for l in df:
            spl = l.split(';')
            d = {
                'valore' : spl[0],
                'data' : spl[1],
                'ora' : spl[2],
                'descrizione' : spl[3]
            }
            dati.append(d)
    return dati

print("bilancio 0.0.1")
out_file = file_output()
print('file:', out_file)
dati = carica_file(out_file)
val_attuale = Decimal('0')
spese_tot = Decimal('0')
guadagni_tot = Decimal('0')
for d in dati:
    m = Decimal(d['valore'])
    val_attuale = val_attuale + m
    if m > Decimal('0'):
        guadagni_tot = guadagni_tot + m
    else:
        spese_tot = spese_tot + m
print('valore attuale:', str(val_attuale))
print('guadagni complessivi:', str(guadagni_tot))
print('spese complessive:', str(spese_tot))
print('grazie.')

