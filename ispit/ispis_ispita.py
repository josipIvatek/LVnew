def ispis_ispita(ispit):
    print(f"\tIspit iz kolegija {ispit['kolegij']['ime']} koji nosi {ispit['kolegij']['ects']} ECTS bodova.")
    print(f"\tIspit će se održati {ispit['datum']}")


def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. Ispit iz kolegija {ispit['kolegij']['ime']}"
