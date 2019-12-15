class Omnibool(object):
    def __eq__(self, x):
        return isinstance(x, bool)
omnibool = Omnibool()

