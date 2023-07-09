import pandas as pd


new_line = ['Kázmér',3,2,5,5,10,0]

class Summary:
    def __init__(self, data):
        self.df = pd.read_csv(data, header=None)
        self.df.loc[len(self.df)] = new_line
        self.df.rename(columns={0: 'Név', 1: 'Magyar', 2: 'Törtenelem', 3: 'Matek', 4: 'Angol',
                                 5: 'Igazolt', 6: 'Igazolatlan'}, inplace=True)

    def __str__(self):
        return f'{self.df}'

    def atlag(self):
        self.df['Átlag'] = self.df.iloc[:,1:5].mean(axis=1)
        print(f'{self.df[["Név","Átlag"]]}')

    @staticmethod
    def thanks(cls):
        print()
        print('Köszönöm szépen a figyelmet !')

my_data = Summary('osztaly.txt')

print(my_data)
print()
my_data.atlag()
my_data.thanks(Summary)