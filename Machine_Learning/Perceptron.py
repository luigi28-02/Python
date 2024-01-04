"""
Nel seguente file verra implementato l' algoritmo
di apprendimento perceptron.
"""
import numpy as np


class Perceptron(object):
    # costruttore
    def __int__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    # metodi
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                print(self.w_)
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:] + self.w_[0])

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


luigi = Perceptron()
