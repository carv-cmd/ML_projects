from sklearn.datasets import make_regression as gen_reg
import numpy as np
import pandas as pd


####################################################
####################################################
class GenData(object):
    """
    Best practice using given 'get' methods to examine class attributes
    Best practice using given 'set' methods for attribute assignment
    Use specific 'get' methods to access 'sample set size', 'number of features', and 'Gaussian noise'
    Use specific 'set' methods to set the attributes listed above individually
    Call 'get_all' method to examine all attributes at once
    Call 'set_all' method to set all parameters at once
    """
    def __init__(self):
        self.df = pd.DataFrame()
        self.n = 100
        self.features = 2
        self.noisy = 25

    def get_n(self):
        """ Returns current attribute reference to sample_Size """
        return self.n

    def get_features(self):
        """ Returns current attribute reference to num_Features """
        return self.features

    def get_noise(self):
        """ Returns current attribute reference to gaussian_Noise """
        return self.noisy

    def get_all(self):
        """ Returns all attributes for the GenData object instance """
        return self.get_n(), self.get_features(), self.get_noise()

    def set_n(self, user_n):
        """ Pass desired sampleSize (integer) to .set_n() method """
        self.n = user_n

    def set_features(self, user_features):
        """ Pass desired sampleSize (integer) to .set_features() method """
        self.features = user_features

    def set_noise(self, user_noise):
        """ Pass desired sampleSize (integer) to .set_noise() method """
        self.noisy = user_noise

    def set_all(self, new_n, new_f, new_no):
        """ 'set_all' method """
        self.set_n(new_n)
        self.set_features(new_f)
        self.set_noise(new_no)


####################################################
####################################################
class GenDataFrame(GenData):
    """
    Generates random dataSets for use with multivariate linear regression models
    GenDataFrame object instance has access to GenData getter/setter methods
    Call "make_df" method to create pd.DataFrame with set/default attributes
    Object created is 'matrix-like' data structure allowing for easy manipulation w/ LinAlg libraries
    """
    def __init__(self):
        super().__init__()

    def auto_gen(self, *args):
        self.set_all(args[0], args[1], args[2])

    def gen_df(self):
        """ Sets the values for gen_reg and creates pandas DataFrame """
        features, y = gen_reg(n_samples=self.get_n(), n_features=self.get_features(), noise=self.get_noise())
        formed = np.concatenate((features, y.reshape(self.get_n(), 1)), axis=1)
        self.df = pd.DataFrame(formed)
        self.df.rename(columns={self.df.columns[-1]: 'y'}, inplace=True)

    def __str__(self):
        """ Returns the DataFrame attributes and df.head(10) """
        df_attrs = [self.df, self.df.shape, self.df.size, self.df.ndim]
        return f'\n--------------DataFrame Attributes--------------\n' \
               f'\n** df.shape:{df_attrs[1]} ' \
               f'** df.size:({df_attrs[2]}) ' \
               f'** df.ndim:({df_attrs[3]}) **' \
               f'\ntype(df): {type(df_attrs[0])}\n' \
               f'\n---------------------------------------------------------\n' \
               f'{df_attrs[0]}' \
               f'\n---------------------------------------------------------\n'


####################################################
####################################################
if __name__ == "__main__":
    def tester_set():
        """
        Initializes GenDataSet object instance
        Prompts for default or custom attribute values
        :returns: Pandas DataFrame object
        """
        daters = GenDataFrame()

        ye_change = ['yes', 'y', 'yes ', 'ys', 'ye', 'es']
        change = str(input("\nWould you like to change to default values? (y/n): ")).lower()
        if change not in ye_change:
            daters.gen_df()
            return daters
        else:
            daters.set_all(50, 6, 25)
            daters.gen_df()
            return daters


    data = tester_set()
    print(data)
