def check_lst_len(lst):
    """
    Function takes input list of integers and return summ of expanded vector.
    Raise exception in case no integer is in list and len of list is
    not correct.
    Input: [1, 4, 3, 4, 5, 3, 1, 5]
    Output: 16
    """
    assert lst
    if len(lst) % 2 == 0:
        sum = 0
        for i in range(1,len(lst),2):
            if not isinstance(lst[i], int):
                raise Exception('{} element of list is not integer'.format(i))
            sum += lst[i]
        return sum
    else:
        raise Exception(("Input list: {} not in sutble format").format(lst))

def multiply_lst(lst1, lst2):
    """
    Function multiply two input lists and return result of multiplying and
    remaining list in case when length of uncompressed vectors are not 
    equal to each other.
    Input: [1 ,4], [3, 5]
    Output: 12, [3, 1]
    """
    assert lst1 and lst2
    res_scal = 0
    a1, a2 = lst1[0], lst1[1]
    b1, b2 = lst2[0], lst2[1]
    
    if a2 > b2:
        res_scal = (a1 * b1) * b2
        rem_lst1 = [a1, a2 - b2]
        rem_lst2 = []
    if a2 < b2:
        res_scal = (a1 * b1) * a2
        rem_lst1 = []
        rem_lst2 = [b1, b2 - a2]
    if a2 == b2:
        res_scal = (a1 * b1) * a2
        rem_lst1 = []
        rem_lst2 = []

    return res_scal, rem_lst1, rem_lst2

def set_next_lst(lst1, lst2, tmp_lst1, tmp_lst2, index1, index2):
    """
    Function takes input lists of compressed vectors, current indexes and 
    remaining list of multiplying.
    Return next lists for multiplying and incremented indexes.
    Input: [1,2,3,4], [1,3,3,1], [],[], 0, 0
    Output: [1,2], [1,3], 2, 2
    """
    assert lst1 and lst2 and index1 >=0 and index2 >=0
    if tmp_lst1:
        new_lst1 = tmp_lst1
        new_lst2 = lst2[index2 : index2 + 2]
        index2 += 2
    elif tmp_lst2:
        new_lst2 = tmp_lst2
        new_lst1 = lst1[index1 : index1 + 2]
        index1 += 2
    else:
        new_lst1 = lst1[index1 : index1 + 2]
        new_lst2 = lst2[index2 : index2 + 2]
        index1 += 2
        index2 += 2

    return new_lst1, new_lst2, index1, index2

def scalar_multiply_lst(l1, l2):
    """
    Function agrigates all logic to calculate scalar multiplying of two 
    compressed vectors.
    Function takes two input lists and return integer number of scalar
    multiplying.
    Input: [1,4,3,4,5,3,1,5], [3,5,4,6,5,5]
    Output: 142
    """
    assert l1 and l2
    result_scal = 0
    rem_lst1 = None
    rem_lst2 = None
    i = 0
    j = 0

    while i < len(l1) or j < len(l2):
        lst1, lst2, i, j = set_next_lst(l1, l2, rem_lst1, rem_lst2, i, j)
        res, rem_lst1, rem_lst2 = multiply_lst(lst1, lst2)
        result_scal += res

    return result_scal

def main():

    l1 = [1, 4, 3, 4, 5, 3, 1, 5]
    l2 = [3, 5, 4, 6, 5, 5]

    if check_lst_len(l1) == check_lst_len(l2):
        scalar = scalar_multiply_lst(l1, l2)
        print(('Result of scalar multiplying of two vectors is: {}').
              format(scalar))
    else:
        raise Exception("Input lists have not equal length to be multiplyed.")

if __name__ == '__main__':
    main()
