#!/data/data/com.termux/files/usr/bin/python

from time import localtime, strftime
from os.path import expanduser, join

def leggiTipo():
    t = input('tipo (+/-) [-]: ')
    if t == '':
        t='-'
    return t

def leggiValore():
    v = ''
    while v == '':
        v = input('valore (#####.##) []: ')
    return v

def leggiData():
    d = input('data (DD/MM/YYYY) [oggi]: ')
    if d == '':
        d = strftime("%d/%m/%Y", localtime())
    return d

def leggiOra():
    o = input('ora (HH:MM) [adesso]: ')
    if o == '':
        o = strftime('%H:%M', localtime())
    return o

def leggiDescrizione():
    d = input('descrizione () []: ')
    return d

def leggiMovimento():
    tipo = leggiTipo()
    valore = leggiValore()
    data = leggiData()
    ora = leggiOra()
    descrizione = leggiDescrizione()
    m = {
        'tipo' : tipo,
        'valore' : valore,
        'data' : data,
        'ora' : ora,
        'descrizione': descrizione
    }
    return m

def scriviMovimento(path, m):
    with open(path, 'a') as f:
        f.write(m['tipo'] + m['valore'])
        f.write(';')
        f.write(m['data'])
        f.write(';')
        f.write(m['ora'])
        f.write(';')
        f.write(m['descrizione'])
        f.write('\n')
    return

print("money 0.0.1")
home = expanduser('~')
out_file_name = 'movimenti.dat'
out_file = join(home, 'dati', out_file_name)
print('file output:', out_file)
m = leggiMovimento()
scriviMovimento(out_file, m)
print('scritto:', m)
print('grazie.')
