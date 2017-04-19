from time import localtime, gmtime, strftime, strptime
from os.path import expanduser, join
from pprint import pprint
from decimal import *

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

def get_file_dati():
    home = expanduser('~')
    nome_file_dati = 'movimenti.dat'
    file_dati = join(home, 'dati', nome_file_dati)
    print('file dati:', file_dati)
    return file_dati

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

def inserimento(file_dati):
    m = leggi_movimento()
    scrivi_movimento(file_dati, m)

def inserimento_dati():
    file_dati = get_file_dati()
    inserimento(file_dati)

def riassunto_dati():
    file_dati = get_file_dati()
    riassunto(file_dati)

def data_default(data):
    try:
        return strptime(data, '%d/%m/%Y')
    except ValueError:
        return gmtime(0)

def ora_default(ora):
    try:
        return strptime(ora, '%H:%M')
    except ValueError:
        return gmtime(0)

def ordina(dati):
    return sorted(
        dati, 
        key = lambda x: (
            data_default(x['data']), 
            ora_default(x['ora'])
        ),
        reverse = True
    )

def riassunto(file_dati):
    dati = carica_file(file_dati)
    dati_ordinati = ordina(dati)
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
    print('ultimi 5 movimenti:')
    for i in range(5):
        if i < len(dati_ordinati):
            print(dati_ordinati[i])
