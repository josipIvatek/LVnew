from datetime import date

kolegiji = []

broj_kolegija = int(input('Unesite broj kolegija: '))

for i in range(1, broj_kolegija+1):
    kolegij = {}
    kolegij['ime'] = input(f"Unesite ime {i}.  kolegija: ")
    kolegij['ects'] = int(input(f"Unesite ECTS bodove za {i}. kolegij: "))
    kolegiji.append(kolegij)

#print('Popis svih kolegija: ')

#for kolegij in kolegiji:
    #print(f"\tKolegij {kolegij['ime']} nosi {kolegij['ects']} ECTS bodova ".expandtabs(8))

ispiti = []
broj_ispita = int(input('Unesite broj ispita: '))
for i in range(1, broj_ispita+1):
    ispit = {}

    for j, kolegij in enumerate(kolegiji, start=1):
        print(f"\t {j}. {kolegij['ime']}")

    odabrani_kolegij=int(input("Unesite kolegij: "))
    ispit['kolegij'] = kolegiji[odabrani_kolegij-1]

    dan = int(input(f"Unesite dan {i}. ispita: "))
    mjesec = int(input(f"Unesite mjesec {i}. ispita: "))
    godina = int(input(f"Unesite godinu {i}.  ispita: "))
    ispit['datum'] = date(godina, mjesec, dan)

    ispiti.append(ispit)

#print("Popis svih ispita: ")
#for ispit in ispiti:
    #print(f"Ispit iz kolegija {ispit['kolegij']['ime']} koji nosi {ispit['kolegij']['ects']} ECTS bodova održat će se {ispit['datum']}")

studenti = []
broj_studenata = int(input('Unesite broj studenata: '))
for k in range(1, broj_studenata+1):
    student = {}
    student['ime'] = input(f"Unesite ime {k}. studenta: ")
    student['prezime'] = input(f"Unesite prezime {k}. studenta: ")
    for l, ispit in enumerate(ispiti, start=1):
        print(f"\t {l}. Ispit iz kolegija {ispit['kolegij']['ime']}")

    odabrani_ispit = int(input("Unesite ispit: "))
    student['ispit'] = ispiti[odabrani_ispit - 1]

    studenti.append(student)

print('popis svih studenata: ')
for student in studenti:
    print(f"\tStudent {student['ime']} {student['prezime']} je prijavio:")
    print(f"\t \t{student['ispit']} koji će se održati {student['ispit']['datum']}")





