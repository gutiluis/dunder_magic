# dunder __getitem__
class X(object):
    def __init__(self):
        self.info = {
            "name": "Goku",
            "country": "Namekusein",
            "number": 1234132
        }
        self.listx = [
            "first_value",
            "second value",
            "third"
        ]


    def __getitem__(self, i):
        return self.info[i]

    def __getitem__(self, a):
        return self.listx[a]


# 1 dictionary. 1 list
# 2 getitem functions.
instance = X()
instance.listx[0]
instance.info["name"]
