import numpy


#
# class for generating linear regression models
#
class LinearRegressor:
    # init with no bias and no weights
    def __init__(self):
        self.weights = 0
        self.bias = 0

    # fit model over 10 iterations and save result
    def fit(self, X, y):
        X = numpy.array(X)
        count = len(X)
        self.weights = [[0] for _ in range(9)]
        for step in range(10):
            y1 = numpy.dot(X, self.weights) + self.bias
            delta_weight = (1 / count) * numpy.dot(X.T, (y1 - y))
            delta_bias = (1 / count) * numpy.sum((y1 - y))
            self.weights = self.weights - (0.1 * delta_weight)
            self.bias = self.bias - (0.1 * delta_bias)

    # generate prediction based on weights and bias determined in fit()
    def predict(self, X):
        return numpy.dot(X, self.weights) + self.bias
