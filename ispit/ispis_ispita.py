def ispis_ispita(ispit):
    print(f"\tIspit iz kolegija {ispit['kolegij']['ime']} koji će se održati {ispit['datum']}.")


def get_ispit(redni_broj, ispit):
    return f"{redni_broj}. Ispit iz kolegija {ispit['kolegij']['ime']}"
