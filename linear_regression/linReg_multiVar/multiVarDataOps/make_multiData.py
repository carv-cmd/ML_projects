from sklearn.datasets import make_regression as gen_reg
import numpy as np
import pandas as pd


####################################################
####################################################
class GenData:
    """
    Generates random multivariate test sets for multivariate linear regression models
    Use singular 'get' methods to access default set size, number of features, and the Gaussian noise
    Use singular 'set' methods to customize data set attributes
    Calls 'set_all' method to set all parameters at once
    Calls "make_df" method to create pd.DataFrame with given attributes
    """

    def __init__(self, n=25, features=2, noisy=25):
        self.df = pd.DataFrame()
        self.n = n
        self.features = features
        self.noisy = noisy

    def get_n(self):
        return self.n

    def get_features(self):
        return self.features

    def get_noise(self):
        return self.noisy

    def set_n(self, user_n=25):
        self.n = user_n

    def set_features(self, user_features=1):
        self.features = user_features

    def set_noise(self, user_noise=10):
        self.noisy = user_noise

    def set_all(self, user_n=15, user_feats=2, user_noise=10):
        user_n = int(input("Enter the desired set size: "))
        user_feats = int(input("Enter the desired number of features: "))
        user_noise = int(input("Enter the desired noise: "))
        self.set_n(user_n)
        self.set_features(user_feats)
        self.set_noise(user_noise)

    def make_df(self):
        features, y = gen_reg(n_samples=self.get_n(), n_features=self.get_features(), noise=self.get_noise())
        formed = np.concatenate((features, y.reshape(self.get_n(), 1)), axis=1)
        self.df = pd.DataFrame(formed)

    def __str__(self):
        return f'\nSetSize:({self.n}) :: ' \
               f'NumFeatures:({self.features}) :: ' \
               f'Noise:({self.noisy})' \
               f'\ndf.shape: {self.df.shape}, ' \
               f'df.size: {self.df.size}, ' \
               f'df.ndim: {self.df.ndim}\n' \
               f'\n{self.df}'


def tester_set():
    dp = GenData()
    dp.set_all()
    dp.make_df()
    return dp


dataSet = tester_set()
print(type(dataSet))
