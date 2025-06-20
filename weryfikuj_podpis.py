from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

# Wczytaj klucz publiczny
with open("klucz_publiczny.pem", "rb") as f:
    public_key = serialization.load_pem_public_key(f.read())

# Wczytaj dane i podpis
with open("plik_do_podpisania.txt", "rb") as f:
    dane = f.read()

with open("podpis.bin", "rb") as f:
    podpis = f.read()

# Weryfikacja
try:
    public_key.verify(
        podpis,
        dane,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("✅ Podpis jest poprawny.")
except Exception as e:
    print("❌ Podpis jest niepoprawny.")
