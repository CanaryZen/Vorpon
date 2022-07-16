import os
import hashlib
from os import system, name
from time import sleep
from os.path import exists

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

file_exists = exists('config/bios.vpb')
if file_exists == True:
    try:
        os.chdir('config')
        if name == 'nt':
            system(f'python bios.vpb')
        else:
            system(f'python3 bios.vpb')
    except:
        a = 'The BIOS File (Which Boots Certain Games) \'bios.vpb\' is corrupted. Please re-download Advanche Vorpon.'
        b = type(a).__name__.encode()
        c = hashlib.sha256(b).hexdigest().upper()[:4]
        while True:
            clear()
            print('[BIOS ERROR] An error has occured while trying to load the BIOS.')
            print(f'[BIOS ERROR] ERROR CODE: 0x{c}')
            print(f'[BIOS ERROR] ERROR MESSAGE: {a}')
            sleep(1)
else:
    a = 'The BIOS File (Which Boots Certain Games) \'bios.vpb\' was not found. Please re-download Advanche Vorpon.'
    b = type(a).__name__.encode()
    c = hashlib.sha256(b).hexdigest().upper()[:4]
    try:
        while True:
            clear()
            print('[BIOS ERROR] An error has occured while trying to load the BIOS.')
            print(f'[BIOS ERROR] ERROR CODE: 0x{c}')
            print(f'[BIOS ERROR] ERROR MESSAGE: {a}')
            sleep(1)
    except KeyboardInterrupt:
        exit()