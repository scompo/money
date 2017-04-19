from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding = 'utf-8') as f:
    long_description = f.read()

setup(
    name = 'money',
    version = '0.0.1',
    description = 'gestisce spese e entrate',
    long_description = long_description,
    url = 'https://github.com/scompo/money',
    author = 'Mauro Scomparin',
    author_email = 'scompo@gmail.com',
    license = 'BSD',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'utils', 'scripts']),
    entry_points={
        'console_scripts' : [
            'inserisci=money.money:inserimento_dati',
            'riassunto=money.money:riassunto_dati',
        ],
    },
)