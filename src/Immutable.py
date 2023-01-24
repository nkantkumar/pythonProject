########################################################################
class Immutable(object):
    """
    An immutable class
    """
    __slots__ = ["one", "two", "three"]

    #----------------------------------------------------------------------
    def __init__(self, one, two, three):
        """Constructor"""
        super(Immutable, self).__setattr__("one", one)
        super(Immutable, self).__setattr__("two", two)
        super(Immutable, self).__setattr__("three", three)

    #----------------------------------------------------------------------
    def __setattr__(self, name, value):
        """"""
        msg = "'%s' has no attribute %s" % (self.__class__,
                                            name)
        raise AttributeError(msg)