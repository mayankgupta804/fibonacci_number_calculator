'''
calculates the fibonacci number for Nth position in the fibonacci sequence 
considering the fibonacco sequence begins as [1, 1...] and not[0, 1...]
'''
def calculate_fibonacci_number(pos):
    '''
    params:
    pos is any position in the fibonacci sequence
    '''
    num = int(pos)
    a = 1
    b = 1
    if num < 0: 
        return -1
    elif num == 0: 
        return a 
    elif num == 1: 
        return b 
    else: 
        for _ in range(2, num): 
            c = a + b 
            a = b 
            b = c 
        return b 