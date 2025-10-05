def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        input_file = open(file_path, "r", encoding="utf-8")
        import csv
        from csv import reader
        reader = csv.reader(input_file)
        input_file.readline()
        dizionario = {}
        for riga in reader:
            dizionario[riga[0]] = riga[1:]
        input_file.close()
        return dizionario
    except FileNotFoundError:
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    import csv
    file = open(file_path, "a", newline="", encoding="utf-8")
    if sezione > 5 or sezione < 0:
        return None
    elif titolo in biblioteca:
        return None
    try:
        biblioteca.update({titolo: [autore, anno, pagine, sezione]})
        writer = csv.writer(file)
        dati = [titolo, autore, anno, pagine, sezione]
        writer.writerow([titolo, autore, anno, pagine, sezione])
        return True
    except FileNotFoundError:
        return None
    file.close()


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    if titolo not in biblioteca:
        return None
    else:
        libro = [titolo, biblioteca[titolo]]
        stringa = ""
        for i in biblioteca[titolo]:
            stringa = stringa + str(i) + ', '
        return stringa.strip(", ")


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    lista = []
    if sezione > 5 or sezione < 0:
        return None
    for i in biblioteca:
        if int(biblioteca[i][3]) == sezione:
            lista.append(i)
    lista_ord = sorted(lista)
    return lista_ord


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

