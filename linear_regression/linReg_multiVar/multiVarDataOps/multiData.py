from make_multiData import *


class SameSets(GenDataFrame):
    """ iterator class to create same dims different values DataSets"""

    def __init__(self):
        super().__init__()
        self.n = 100
        self.feats = 2
        self.noice = 25
        self.listed = []

    def append_listed(self, new_daters):
        self.listed.append(new_daters)

    def same_sets(self):
        dati = GenDataFrame()
        dati.auto_gen(self.n, self.feats, self.noice)
        dati.gen_df()
        return dati

    def same_sets_marriage(self, num=5):
        for i in range(num):
            datuh = self.same_sets()
            self.append_listed(datuh.df)


####################################################
####################################################
if __name__ == '__main__':
    s_list = SameSets()
    s_list.set_n(6)
    s_list.same_sets_marriage()
    for elem in s_list.listed:
        print(f'\n---------------------------------------------------------'
              f'\n{elem}'
              f'\n---------------------------------------------------------')
