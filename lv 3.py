kolegiji = []

broj_kolegija = int(input('Unesite broj kolegija: '))

for i in range(broj_kolegija):
    kolegij = {}
    kolegij['ime'] = input('Unesite ime kolegija: ')
    kolegij['ects'] = int(input(f"Unesite ECTS bodove za {i+1}. kolegij: "))
    kolegiji.append(kolegij)

print('Popis svih kolegija: ')

for kolegij in kolegiji:
    print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova ".expandtabs(8))
