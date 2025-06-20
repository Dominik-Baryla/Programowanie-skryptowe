# ✍️ Podpis Cyfrowy Pliku (Python)

Ten projekt demonstruje, jak za pomocą języka Python można:

🔐 Wygenerować klucze RSA  
📝 Podpisać cyfrowo plik  
✅ Zweryfikować podpis cyfrowy

## 📁 Struktura projektu

- `podpisz_plik.py` – generuje klucze i podpisuje plik
- `weryfikuj_podpis.py` – weryfikuje podpis pliku
- `plik_do_podpisania.txt` – plik wejściowy do podpisania
- `podpis.bin` – podpisany hash pliku (tworzy się po uruchomieniu)
- `klucz_publiczny.pem`, `klucz_prywatny.pem` – klucze RSA

## ⚙️ Wymagania

```bash
pip install cryptography
```

## ▶️ Uruchomienie

### 1. Podpisz plik

```bash
python podpisz_plik.py
```

📷 Po uruchomieniu zostaną wygenerowane klucze i plik `podpis.bin`.

### 2. Zweryfikuj podpis

```bash
python weryfikuj_podpis.py
```

✅ Otrzymasz informację, czy podpis jest poprawny.

---

## 🖼️ Zrzuty ekranu

| Podpis | Weryfikacja |
|--------|-------------|
| ![Podpis](screenshots/podpis.png) | ![Weryfikacja](screenshots/weryfikacja.png) |

---

## 📌 Autor

Projekt edukacyjny przygotowany na potrzeby zadania z podpisu cyfrowego.
