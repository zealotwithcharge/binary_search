from binary_search import find_smallest_positive, count_repeats, argmin
import timeit



def test__find_smallest_positive_1():
    assert find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])==4

def test__find_smallest_positive_2():
    assert find_smallest_positive([0, 1, 2, 3])==1

def test__find_smallest_positive_3():
    assert find_smallest_positive([-3, -2, -1, 0, 1])==4

def test__find_smallest_positive_4():
    assert find_smallest_positive([-3, -2, -1, 0, 0.1, 1])==4

def test__find_smallest_positive_5():
    assert find_smallest_positive([]) is None

def test__find_smallest_positive_6():
    assert find_smallest_positive([-1]) is None

def test__find_smallest_positive_7():
    assert find_smallest_positive([1]) == 0

def test__find_smallest_positive_8():
    assert find_smallest_positive([1, 2]) == 0

def test__find_smallest_positive_9():
    assert find_smallest_positive([-1, 2]) == 1

def test__find_smallest_positive_10():
    assert find_smallest_positive([-2, -1]) is None



def test__count_repeats_1():
    assert count_repeats([1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1)==10

def test__count_repeats_2():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],1)==10

def test__count_repeats_3():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],1)==10

def test__count_repeats_4():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],2)==5

def test__count_repeats_5():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],5)==1

def test__count_repeats_6():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, -1],-1)==1

def test__count_repeats_7():
    assert count_repeats([5, 4, 3, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 1],-1)==0

def test__count_repeats_8():
    assert count_repeats([5],1)==0

def test__count_repeats_9():
    assert count_repeats([5],5)==1

def test__count_repeats_10():
    assert count_repeats([],5)==0



def test__argmin_1():
    epsilon = 1.0
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_2():
    epsilon = 1e-3
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_3():
    epsilon = 1e-6
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_4():
    epsilon = 1e-9
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_5():
    epsilon = 1e-12
    lo = -20
    hi = 20
    x_min = 5
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_6():
    epsilon = 1e-6
    lo = -1e20
    hi = 1e20
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_7():
    epsilon = 1e-6
    lo = -1e20
    hi = 0
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon

def test__argmin_8():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = 5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-x_min) <= epsilon

def test__argmin_9():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = -5000
    f = lambda x: (x-x_min)**2
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon

def test__argmin_10():
    epsilon = 1e-6
    lo = 0
    hi = 1e20
    x_min = -5000
    f = lambda x: x
    assert abs(argmin(f,lo,hi,epsilon)-0) <= epsilon


# the following test ensure that the runtimes are logrithmic

def test__find_smallest_positive_runtime():
    seconds = timeit.timeit(
        'find_smallest_positive(xs)',
        'from binary_search import find_smallest_positive; xs=list(range(-100000,100000,1))'
        )
    print('seconds=',seconds)
    return True

def test__count_repeats_runtime():
    seconds = timeit.timeit(
        'count_repeats(xs,0)',
        'from binary_search import count_repeats; xs=list(range(100000,-100000,-1))'
        )
    print('seconds=',seconds)
    return True
