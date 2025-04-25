def stair_case(n):
    if n <=2:
       if n == 0:
          return 1
       return n
    
    return stair_case(n-1) + stair_case (n-2) + stair_case (n-3)



if __name__ == '__main__':
   expectation = [1,2,4,7,13]

   for i, x in enumerate(expectation):
       stair_case(i) == x
       print('ok')