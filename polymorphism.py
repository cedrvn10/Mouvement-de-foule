from numpy import sqrt


class MyTuple(tuple):
    def add(self, tuple2):
        return tuple(map(lambda i, j: i + j, self, tuple2))

    def substract(self, tuple2):
        return tuple(map(lambda i, j: i - j, self, tuple2))

    def square_distance(self, tuple2):
        return sqrt(sum(map(lambda i, j: (i - j) ** 2, self, tuple2)))
