# Copyright (C) 2004-2011, Parrot Foundation.
class Foo:
    def __init__(self):
	self.i = 10
	self.j = 20

class main:
    for i in range(1,500000):
	o = Foo()
    o = Foo()
    print o.i

