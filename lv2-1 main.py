
from datetime import date
kolegij = {}

kolegij['ime']=input('Unesite ime kolegija: ').upper()
kolegij['ects']=int(input('Unesite ECTS bodove za kolegij: '))

# print('Kolegij', kolegij['ime'], 'nosi', kolegij['ects'], 'ECTS bodova.')
ispit={}
dan=int(input('Unesite dan ispita: '))
mjesec=int(input('Unesite mjesec ispita: '))
godina=int(input('Unesite godinu ispita: '))
ispit['kolegij']=kolegij
ispit['datum']=date(godina,mjesec,dan)

# print('Kolegij', ispit['kolegij']['ime'], 'nosi', ispit['kolegij']['ects'], 'ECTS bodova. ')
# print('Datum ispita je', ispit['datum'])

student={}
student['ispit']=ispit
student['kolegij']=kolegij
student['ime']=input('Unesite ime studenta: ').capitalize()
student['prezime']=input('Unesite prezime studenta: ').capitalize()

print('Student ', student['ime'], student['prezime'])
print('je prijavio ispit iz kolegija ', student['kolegij']['ime'])
print('koji će se održati:', student['ispit']['datum'])

