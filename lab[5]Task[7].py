class kangaroo(object):

    def __init__(self, pouch=[]):
        self.pouch = pouch

    def put_in_pouch(self, ob):
        self.pouch = ob

    def __str__(self):
        return (self, self.pouch)


k1 = kangaroo()
k2 = kangaroo()

kang = k1
roo = k2

kang.put_in_pouch(roo)

print(kang.__str__())




