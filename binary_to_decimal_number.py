def binary_array_to_number(arr):
    ''' Take list with binary number, sample: [0,1,1,0].
        Give decimal number.
    '''
    count = len(arr) - 1
    sum_arr = 0
    for i in arr:
        sum_arr += i * (2 ** count)
        count -= 1
    return sum_arr
