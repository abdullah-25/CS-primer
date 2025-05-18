"""
problem: 
- 2 lists side by side
- find diff of smallest on left with smallest on right and store
- keep doing this and add up all diff
- retun diff

plan:
- sort list A, sort list B
  - break down input and create a list of A and B
- iterate over it and find diff

"""

from input_data import PUZZLE_INPUT

def day1_part1(input_data):
    """
    Process the puzzle input for part 1.
    
    Args:
        input_data (str): The raw puzzle input string
        
    Returns:
        int: The calculated difference between sorted values
    """
    diff = 0
    list_a = []
    list_b = []
    input_data = input_data.strip().split('\n')
    for line in input_data:
        if line:
            parts = line.split()
            list_a.append(parts[0])
            list_b.append(parts[1])

    list_a.sort()
    list_b.sort()

    for i in enumerate(list_a):
        diff += abs(int(list_a[i]) - int(list_b[i]))

    return diff

def day1_part2(input_data):
    """
    Process the puzzle input for part 2.
    
    Args:
        input_data (str): The raw puzzle input string
        
    Returns:
        int: The calculated similarity score
    """
    sim_score = 0
    list_a = []
    list_b = []
    input_data = input_data.strip().split('\n')
    for line in input_data:
        if line:
            parts = line.split()
            list_a.append(parts[0])
            list_b.append(parts[1])

    counter = 0

    for i in (list_a):
        for j in (list_b):
            if int(i) == int(j):
                counter += 1
            sim_score += counter * int(i)
            counter = 0
        sim_score += counter * int(i)

    return sim_score


print(day1_part2(PUZZLE_INPUT))
