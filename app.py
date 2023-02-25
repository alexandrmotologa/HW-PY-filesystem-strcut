# Definim două liste, una pentru directoare și alta pentru subdirectoare
disk = [
    "home",
    "system",
    "config",
    "backup",
]
home_folder = [
    "pictures",
    "music",
    "docs",
]

# Afisam linia de start
print("/-.")

# Pentru fiecare director din lista "disk"
for directory in disk:
    # Dacă directorul este "home", setam sufixul pentru a indica acest lucru
    suf = " -." if directory == "home" else ""

    # Afisam numele directorului, împreună cu sufixul, dacă există
    print("  +-- " + directory + suf)

    # Dacă directorul este "home", afișăm subdirectoarele din lista "home_folder"
    if directory == "home":
        for subdirectory in home_folder:
            # Afișam fiecare subdirector împreună cu un spațiu pentru indentare
            print("  |         +-- ", subdirectory)

            # Dacă subdirectorul nu este ultimul din lista, afișăm o linie verticală suplimentară
            if subdirectory != home_folder[-1]:
                print("  |         |")

    # Dacă directorul nu este ultimul din lista, afișăm o linie verticală pentru separare
    if directory != disk[-1]:
        print("  |")