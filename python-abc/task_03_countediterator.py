class CountedIterator:
    
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def get_count(self):
        return self.count
    
    def __next__(self):
        try:
            item = next(self.iterator)
        except:
            raise StopIteration
        self.count += 1
        return item
