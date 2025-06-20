from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes 
from cryptography.hazmat.primitives import padding 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import os
import hashlib

# Ustawienia
HASLO = b'moje_super_tajne_haslo'
SOL = os.urandom(16)
WEKTOR_IV = os.urandom(16)

def uzyskaj_klucz(haslo, sol):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=sol,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(haslo)


def zaszyfruj_plik(nazwa_pliku, nazwa_wyjscia):
    with open(nazwa_pliku, 'rb') as plik:
        dane = plik.read()

    wypelniacz = padding.PKCS7(128).padder()
    dane_wypelnione = wypelniacz.update(dane) + wypelniacz.finalize()

    klucz = uzyskaj_klucz(HASLO, SOL)
    szyfr = Cipher(algorithms.AES(klucz), modes.CBC(WEKTOR_IV), backend=default_backend())
    szyfrator = szyfr.encryptor()
    dane_zaszyfrowane = szyfrator.update(dane_wypelnione) + szyfrator.finalize()

    with open(nazwa_wyjscia, 'wb') as plik_wyjscie:
        plik_wyjscie.write(SOL + WEKTOR_IV + dane_zaszyfrowane)

def odszyfruj_plik(nazwa_pliku, nazwa_wyjscia):
    with open(nazwa_pliku, 'rb') as plik:
        surowe_dane = plik.read()

    sol = surowe_dane[:16]
    wektor_iv = surowe_dane[16:32]
    dane_zaszyfrowane = surowe_dane[32:]

    klucz = uzyskaj_klucz(HASLO, sol)
    szyfr = Cipher(algorithms.AES(klucz), modes.CBC(wektor_iv), backend=default_backend())
    deszyfrator = szyfr.decryptor()
    dane_wypelnione = deszyfrator.update(dane_zaszyfrowane) + deszyfrator.finalize()

    usuwacz_wypelnienia = padding.PKCS7(128).unpadder()
    dane = usuwacz_wypelnienia.update(dane_wypelnione) + usuwacz_wypelnienia.finalize()

    with open(nazwa_wyjscia, 'wb') as plik_wyjscie:
        plik_wyjscie.write(dane)

if __name__ == "__main__":
    zaszyfruj_plik('wejscie.txt', 'zaszyfrowane.bin')
    odszyfruj_plik('zaszyfrowane.bin', 'odszyfrowane.txt')
    print("Plik został zaszyfrowany i odszyfrowany pomyślnie.")
