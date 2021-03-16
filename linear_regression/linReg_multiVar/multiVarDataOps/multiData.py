from make_multiData import *


class SameSets(GenDataFrame):
    """
    iterator class to create same dims different values DataSets
    Create object instance and specify any of the GenData attributes desired
    """
    def __init__(self):
        super().__init__()
        self.listed = []
        self.num = 5

    def get_num(self):
        """ 'get' the current range for the iterator object """
        return self.num

    def set_num(self, new_range):
        """ 'set' the current range for the iterator object """
        self.num = new_range

    def append_listed(self, new_daters):
        """ Append GenDataFrame object to SameSets class instance list """
        self.listed.append(new_daters)

    def same_sets(self):
        """ Called by same_sets_marriage to initialize GenDataFrame object for use """
        dati = GenDataFrame()
        dati.auto_gen(self.get_n(), self.get_features(), self.get_noise())
        dati.gen_df()
        return dati

    def same_sets_marriage(self):
        """ Iterates over a given range creating identical dim dataSets """
        for i in range(self.get_num()):
            datuh = self.same_sets()
            self.append_listed(datuh.df)

    def get_listed(self):
        """ Returns list object of GenData DataFrame objects """
        return self.listed


####################################################
####################################################
if __name__ == '__main__':
    same_list = SameSets()
    same_list.set_num(15)
    same_list.set_all(12, 6, 5)
    same_list.same_sets_marriage()
    for elem in same_list.get_listed():
        print(f'\n---------------------------------------------------------'
              f'\n{elem.head()}'
              f'\n---------------------------------------------------------')
