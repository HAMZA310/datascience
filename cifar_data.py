import numpy as np
import pickle
import os

def one_hot(vec, vals=10):
    n = len(vec)
    out = np.zeros((n, vals))
    out[range(n), vec] = 1
    return out

def unpickle(file):
    with open(os.path.join(DATA_PATH, file), 'rb') as fo:
        u = pickle._Unpickler(fo)   
        u.encoding = 'latin1'
        dct = u.load()
    return dct

class CifarLoader(object):

    def __init__(self, source_files):
        self._source = source_files
        self._i = 0
        self.images = None
        self.labels = None

    def load(self):
        data = [unpickle(f) for f in self._source]
        images = np.vstack([d["data"] for d in data])
        n = len(images)
        self.images = images.reshape(n, 3, 32, 32).transpose(0, 2, 3, 1)\
            .astype(float) / 255
        self.labels = one_hot(np.hstack([d["labels"] for d in data]), 10)
        return self

    def next_batch(self, batch_size):
        x, y = self.images[self._i:self._i+batch_size], \
               self.labels[self._i:self._i+batch_size]
        self._i = (self._i + batch_size) % len(self.images)
        return x, y

    def random_batch(self, batch_size):
        n = len(self.images)
        ix = np.random.choice(n, batch_size)
        return self.images[ix], self.labels[ix]

class CifarDataManager(object):
    def __init__(self):
        self.train = CifarLoader(["data_batch_{}".format(i) for i in range(1, 6)])\
            .load()
        self.test = CifarLoader(["test_batch"]).load()

DATA_PATH = "CIFAR10_data/"
d = CifarDataManager()
images = d.train.images
