class X(object):
    def __init__(self):
        self.info = [
            "first value",
            "second value"
        ]
    def __add__(self, a):
        return self.info(a)


instance = X()
# how to adde it in a permanent list?
instance.info.__add__(["insert in list"])
