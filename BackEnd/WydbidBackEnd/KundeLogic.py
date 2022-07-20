import Wydbid
import os

def setupKundenFolder():
    kunden_path = f'{Wydbid.firmen_location}Kunden'

    if os.path.exists(kunden_path):
        return
    else:
        os.mkdir(kunden_path)