class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not hasattr(self, 'iterated'):
            self.iterated = False
            return {'length': self.length}
        elif not self.iterated:
            self.iterated = True
            return {'width': self.width}
        else:
            raise StopIteration