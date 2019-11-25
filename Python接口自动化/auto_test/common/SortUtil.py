class SortItem(object):
    def __init__(self, obj, reverse=False):
        self.obj = obj
        self.reverse = reverse

    def __lt__(self, other):
        if self.obj is None:
            if isinstance(other.obj, int):
                self.obj = 0.1
            elif isinstance(other.obj, str):
                self.obj = ""
            else:
                pass
        return self.obj < other.obj if self.reverse is False else self.obj > other.obj

    def __eq__(self, other):
        if self.obj is None:
            if isinstance(other.obj, int):
                self.obj = 0.1
            elif isinstance(other.obj, str):
                self.obj = ""
            else:
                pass
        return self.obj == other.obj

    def __gt__(self, other):
        if self.obj is None:
            if isinstance(other.obj, int):
                self.obj = 0.1
            elif isinstance(other.obj, str):
                self.obj = ""
            else:
                pass
        return self.obj > other.obj if self.reverse is False else self.obj < other.obj