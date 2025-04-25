import csv

class MemoryScan(object):
    """
    Yield all records from the given "table" in memory.

    This is really just for testing... in the future our scan nodes
    will read from disk.
    """
    def __init__(self, table):
        self.table = table
        self.idx = 0

    def next(self):
        if self.idx >= len(self.table):
            return None

        x = self.table[self.idx]
        self.idx += 1
        return x

class CSVfilereader(object):
    def __init__(self, filename, schema):
        self.filename = filename
        self.schema = schema
        self.file = None
        self.reader = None
    
    def next(self):
        if self.file is None:
            self.file = open(self.filename)
            self.reader = csv.reader(self.file)
            next(self.reader)
        
        try:
            row = next(self.reader)
            converted_row = []

            for i in range(len(self.schema)):
                changed_type = self.schema[i](row[i])
                converted_row.append(changed_type)

            return tuple(converted_row)
        
        except StopIteration:
            self.file.close()
            return None


class Projection(object):
    """
    Map the child records using the given map function, e.g. to return a subset
    of the fields.
    """
    def __init__(self, proj):
        self.proj = proj

    def next(self):
        x = self.child.next()
        if x is None:
            return None
        return self.proj(x)


class Selection(object):
    """
    Filter the child records using the given predicate function.

    Yes it's confusing to call this "selection" as it's unrelated to SELECT in
    SQL, and is more like the WHERE clause. We keep the naming to be consistent
    with the literature.
    """
    def __init__(self, predicate):
        self.predicate = predicate

    def next(self):
        while True:
            x = self.child.next()
            if x is None or self.predicate(x):
                return x
            

class Limit(object):
    """
    Return only as many as the limit, then stop
    """
    def __init__(self, n):
        self.n = n
        self.child = None  # Add child attribute
    
    def next(self):
        if self.n <= 0:  
            raise StopIteration  
            
        self.n -= 1
        return self.child.next() 

class Sort(object):
    """
    Sort based on the given key function
    """
    def __init__(self, key, desc=False):
        self.key = key
        self.desc = desc
        self.items = []
        self.idx = 0
        

    def next(self):
        if self.items is []:
            while True:
                x = self.child.next()
                if x is None:
                    break
                self.items.append(x)
            self.tuples.sort(key=self.key, reversed=self.desc)
        
        if self.idx > len(self.tuples):
            return None
        item = self.tuples(self.idx)
        self.idx += 1
        return item



def Q(*nodes):
    """
    Construct a linked list of executor nodes from the given arguments,
    starting with a root node, and adding references to each child
    """
    ns = iter(nodes)
    parent = root = next(ns)
    for n in ns:
        parent.child = n
        parent = n
    return root


def run(q):
    """
    Run the given query to completion by calling `next` on the (presumed) root
    """
    while True:
        x = q.next()
        if x is None:
            break
        yield x


if __name__ == '__main__':
    movies_schema = (id, str, str)
    f = run(Q(
       Limit(4),
       CSVfilereader('movies.csv',movies_schema),
        
    ))
    print((f))
    print('ok')