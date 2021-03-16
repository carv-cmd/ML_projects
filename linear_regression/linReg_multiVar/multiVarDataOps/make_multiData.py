import logging as logs
from sklearn.datasets import make_regression as gen_reg
import pandas as pd
import matplotlib.pyplot as plt


####################################################
####################################################
class GenData:

    def __init__(self, n=25, features=1, noisy=25):
        self.dps = pd.DataFrame
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

    def __str__(self):
        return f'\nSetSize:({self.n}) :: ' \
               f'NumFeatures:({self.features}) :: ' \
               f'Noise:({self.noisy})'


def tester_set():
    dp = GenData()
    dp.set_n(25)
    dp.set_features(2)
    dp.set_noise(15)

    print(dp.__str__())


tester_set()

# dati = 150
# feats = 6
#
# features, y = reg_func(n_samples=dati, n_features=feats, noise=25)
# formed = np.concatenate((features, y.reshape(dati, 1)), axis=1)
# df = pd.DataFrame(formed)
#
# print(f'\nDataFrame_TestSet: '
#       f'\nndim={df.ndim}, shape={df.shape}, size={df.size}\n'
#       f'\n{df}')

