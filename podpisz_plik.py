from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

# 1. Wygeneruj klucz prywatny i publiczny
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# 2. Zapisz klucze do plików
with open("klucz_prywatny.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("klucz_publiczny.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# 3. Wczytaj dane z pliku do podpisania
nazwa_pliku = "plik_do_podpisania.txt"

with open(nazwa_pliku, "rb") as f:
    dane = f.read()

# 4. Podpisz dane
podpis = private_key.sign(
    dane,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# 5. Zapisz podpis do pliku
with open("podpis.bin", "wb") as f:
    f.write(podpis)

print("✅ Plik został podpisany cyfrowo.")
