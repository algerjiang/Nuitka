#
#     Kay Hayen, mailto:kayhayen@gmx.de
#
#     Python test originally created or extracted from other peoples work. The
#     parts from me are in the public domain. It is at least Free Software
#     where it's copied from other people. In these cases, it will normally be
#     indicated.
#
#     If you submit Kay Hayen patches to this software in either form, you
#     automatically grant him a copyright assignment to the code, or in the
#     alternative a BSD license to the code, should your jurisdiction prevent
#     this. Obviously it won't affect code that comes to him indirectly or
#     code you don't submit to him.
#
#     This is to reserve my ability to re-license the code at any time, e.g.
#     the PSF. With this version of Nuitka, using it for Closed Source will
#     not be allowed.
#
#     Please leave the whole of this copyright notice intact.
#
def dictOrderCheck():
    def key1():
        print "key1 called"

        return 1
    def key2():
        print "key2 called"

        return 2
    def value1():
        print "value1 called"

        return 11
    def value2():
        print "value2 called"

        return 22

    print "Checking order of calls in dictionary creation from callables:"

    print { key1() : value1(), key2() : value2() }

def listOrderCheck():
    def value1():
        print "value1 called"

        return 11
    def value2():
        print "value2 called"

        return 22

    print [ value1(), value2() ]

def sliceOrderCheck():
    d = range(10)

    def lvalue():
        print "lvalue",

        return d

    def rvalue():
        print "rvalue",

        return range(2)

    def low():
        print "low",

        return 0

    def high():
        print "high",

        return 4

    def step():
        print "step",

        return 2

    print lvalue()[ low() : high() : step() ]

    lvalue()[ low() : high() : step() ] = rvalue()
    print d

    del lvalue()[ low() : high() : step() ]
    print d

def subscriptOrderCheck():
    d={}

    def lvalue():
        print "lvalue",

        return d

    def rvalue():
        print "rvalue",

        return 2

    def subscript():
        print "subscript",

        return 1

    lvalue()[ subscript() ] = rvalue()
    print d

    print lvalue()[ subscript() ]

    del lvalue()[ subscript() ]
    print d

def compareOrderCheck():
    def lvalue():
        print "lvalue",

        return 1

    def rvalue():
        print "rvalue",

        return 2

    print "==", lvalue() == rvalue()
    print "<=", lvalue() <= rvalue()
    print ">=", lvalue() >= rvalue()
    print "!=", lvalue() != rvalue()
    print ">", lvalue() > rvalue()
    print "<", lvalue() < rvalue()

dictOrderCheck()
listOrderCheck()
subscriptOrderCheck()
compareOrderCheck()
sliceOrderCheck()
