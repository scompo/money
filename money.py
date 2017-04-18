from time import localtime, strftime
from os.path import expanduser, join
from pprint import pprint

def leggi_tipo():
    t = 'n'
    while not (t == '' or t == '+' or t == '-'):
        t = input('tipo (+/-) [-]: ')
    if t == '':
        t='-'
    elif t == '+':
        t=''
    return t

def leggi_valore():
    v = ''
    while v == '':
        v = input('valore (#####.##) []: ')
    return v

def leggi_data():
    d = input('data (DD/MM/YYYY) [oggi]: ')
    if d == '':
        d = strftime("%d/%m/%Y", localtime())
    return d

def leggi_ora():
    o = input('ora (HH:MM) [adesso]: ')
    if o == '':
        o = strftime('%H:%M', localtime())
    return o

def leggi_descrizione():
    d = input('descrizione () []: ')
    return d

def leggi_movimento():
    tipo = leggi_tipo()
    valore = leggi_valore()
    data = leggi_data()
    ora = leggi_ora()
    descrizione = leggi_descrizione()
    m = {
        'tipo' : tipo,
        'valore' : valore,
        'data' : data,
        'ora' : ora,
        'descrizione': descrizione
    }
    return m

def scrivi_movimento(path, m):
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

def file_output():
    home = expanduser('~')
    out_file_name = 'movimenti.dat'
    out_file = join(home, 'dati', out_file_name)
    return out_file

print("money 0.0.1")
out_file = file_output()
print('file output:', out_file)
m = leggi_movimento()
scrivi_movimento(out_file, m)
print('scritto:')
pprint(m)
print('grazie.')

