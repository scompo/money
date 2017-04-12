from decimal import *

dati = []
stato = 0
with open('dati.quif','r') as f:
    for l in f:
        if stato == 0 and '!Type:Cash' in l:
            stato = 1
            tr = {
                    'head' : l
            }
            dati.append(tr)
        elif stato == 1 and l.startswith('D'):
            dati[-1]['data'] = l
        elif stato == 1 and l.startswith('M'):
            dati[-1]['descrizione'] = l
        elif stato == 1 and l.startswith('$'):
            dati[-1]['importo'] = l
        elif stato == 1 and '^' in l:
            stato = 0

for d in dati:
    data = d['data'][1:].replace('\n','')
    descrizione = d['descrizione'][1:].replace('\n','')
    importo = d['importo'][1:].replace('\n', '').replace(',', '.')
    imp_ok = Decimal(importo) * Decimal('-1')
    print(str(imp_ok) + ';' + data + ';' + ';' + descrizione)

