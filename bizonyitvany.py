class Bizonyitvany():
    def __init__(self, nev, magyar, tortenelem, matek, angol, igazolt, igazolatlan):
        self.nev = nev
        self.magyar = int(magyar)
        self.tortenelem = int(tortenelem)
        self.matek = int(matek)
        self.angol = int(angol)
        self.igazolt = int(igazolt)
        self.igazolatlan = int(igazolatlan)

    def __str__(self):
        return f'{self.nev:10s} \t\t Magyar: {self.magyar}\t  Tört.: {self.tortenelem}\t  Matek: {self.matek}\t' \
               f'  Nyelv: {self.angol}\t  Ig.: {self.igazolt:3d}, NemIg.:  {self.igazolatlan:}'

    def atlag(self):
        return (self.magyar + self.tortenelem + self.matek + self.angol)/4

my_list = []

my_list.append(Bizonyitvany('Kázmér',3,2,5,5,10,0))
print(*my_list)
with open('osztaly.txt','r',encoding='utf8') as read_file:

    for row in read_file:
        #adat = row.strip().split(',')
        my_list.append(Bizonyitvany(*row.strip().split(',')))

print(f'Feltöltve {len(my_list)} adatsor.')
print('Az osztály naplója:')
for i,j in enumerate(my_list):
    print(f'{i+1}.: {j}')

print('\nA diákok átlagai:')
for i,j in enumerate(my_list):
    print(f'{i+1:2d}. {j.nev:10s}\t: {j.atlag()}')