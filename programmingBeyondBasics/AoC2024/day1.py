"""
part1:

3 4 2 1 3 3
4 3 5 3 9 3

1 2 3 3 3 4
3 3 3 4 5 9

2 1 0 1 2 5

11


plan:
    - for each line in input:
        - parse x and y
        - add ti xs and ys array
    - sort xs and ys
    - iterate over pair in x, y in xs and accum abs(x-y)


part2:

3 4 2 1 3 3
4 3 5 3 9 3

plan:
    - for each number in left
        - find occurance in right side
        - multiply that number with item
        - keep runnin total 
    - return

"""
from collections import Counter 

def one(lines):
    xs, ys = [], []
    for line in lines:
        x, y = line.split('   ')
        xs.append(int(x))
        ys.append(int(y))
    xs.sort()
    ys.sort()

    total = 0
    for i in range(len(xs)):
        total += abs(xs[i] - ys[i])
    return total

def two(lines):
    xs, ys = [], []
    for line in lines:
        x, y = line.split('   ')
        xs.append(int(x))
        ys.append(int(y))
    counts = Counter(ys)
    return sum((counts[x] * x for x in xs))


small_input = """3   4
4   3
2   5
1   3
3   9
3   3"""

print(one(small_input.split('\n')))