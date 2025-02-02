"""
In this problem, you'll apply recursive thinking to a naturally 
recursive structure: an array of arrays. 
Your task will be to "pretty print" the structure, 
that is to say print it with an appropriate amount of indentation 
to show the level of nesting of items in the structure.
"""

def prettyPrint(x):
    if type(x) is list or any(type(item) is list for item in x):
        return converter(x)

    
    
def converter(lst):
    """
    Takes a list and return it in string format
    """
    builder = []
    for item in lst:
        if type(item) is list:
            builder.append(converter(item))
        else:
            builder.append(repr(item))
    return '[' + ',\n '.join(builder) + ']'


if __name__ == "__main__":
    print(converter([1,2,3,[4,5]]))

