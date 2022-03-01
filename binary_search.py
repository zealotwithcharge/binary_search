#! / usr / bin / python3
'''
JOKE: There are 2 hard problems in computer science: cache i
nvalidation, naming things, and off - by -1 errors.

It's really easy to have off - by -1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> find_smallest_positive([ -3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([ -3, -2, -1]) is None
    True
    '''
    if xs == []:
        return
    elif xs[-1] < 0:
        return
    if len(xs) == 0:
        return

    def search(xs):
        mid_index = len(xs) // 2
        if xs[mid_index] == 0:
            return mid_index
        if mid_index == 0:
            if xs[mid_index] <= 0:
                return mid_index
            else:
                return mid_index - 1
        if xs[mid_index] > 0:
            index = search(xs[:mid_index])
            return index
        if xs[mid_index] < 0:
            index = search(xs[mid_index + 1:])
            return index + mid_index + 1

    return search(xs) + 1
#    def search(xs)
#        if len(xs) != 1:
#            mid_index = int(len(xs) / 2)
#            mid = xs[mid_index]
#            if mid > 0:
#                return search(xs[:mid_index])
#            else:
#                return search(xs[mid_index:])
#        else:
#            print(xs)
#            return xs[0]
#    smallest = search(xs)
#    for i, num in enumerate(xs):
#        if smallest > 0:
#            if num == smallest:
#                return i
#        else:
#            if num == smallest:
#                if len(xs) == i + 1:
#                    return
#                else:
#                    return i + 1


def count_repeats(xs, x=1):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand - alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    APPLICATION:
    This is a classic question for technical interviews.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    if xs == []:
        return 0

    def search_up(xs):
        if xs == []:
            return 0
        mid_index = len(xs) // 2
        if mid_index == 0:
            if xs[mid_index] == x:
                return -1
            else:
                return 0
        else:
            if xs[mid_index] <= x:
                return search_up(xs[:mid_index])
            if xs[mid_index] > x:
                if mid_index == len(xs) - 1:
                    return mid_index
                return search_up(xs[mid_index + 1:]) + mid_index + 1

    def search_down(xs):
        if xs == []:
            return 0
        mid_index = len(xs) // 2
        if mid_index == 0:
            if xs[mid_index] == x:
                return 1
            else:
                return 0
        if xs[mid_index] < x:
            if mid_index == 0:
                return mid_index
            index = search_down(xs[:mid_index])
            return index
        if xs[mid_index] >= x:
            index = search_down(xs[mid_index + 1:])
            return index + mid_index + 1
    if xs[-1] == x:
        high_end = len(xs)
    else:
        high_end = search_down(xs)
    if xs[0] == x:
        low_end = -1
    else:
        low_end = search_up(xs)
    if high_end != low_end:
        return high_end - low_end - 1
    else:
        return 0


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float a
s input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value tha
t minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi - lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest,
               you recursively call your function on the int
erval [lo,m2] or [m1,hi]

    APPLICATION:
    Essentially all data mining algorithms are just this arg
min implementation in disguise.
    If you go on to take the data mining class (CS145 / MATH166),
    we will spend a lot of time talking about different f fu
nctions that can be minimized and their applications.
    But the actual minimization code will all be a variant o
f this binary search.

    WARNING:
    The doctests below are not intended to pass on your code,
    and are only given so that you have an example of what t
he output should look like.
    Your output numbers are likely to be slightly different
due to minor implementation details.
    Writing tests for code that uses floating point numbers
is notoriously difficult.
    See the pytests for correct examples.

    >>> argmin(lambda x: (x -5) ** 2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x -5) ** 2, -20, 0)
    -0.00016935087808430278
    '''
    if hi - lo < epsilon:
        return (hi + lo) / 2
    m1 = lo + (hi - lo) / 3
    m2 = hi - (hi - lo) / 3
    point_dict = {f(lo): lo, f(m1): m1, f(m2): m2, f(hi): hi}
    miner = point_dict[min(point_dict.keys())]
    if miner == lo or miner == m1:
        return argmin(f, lo, m2, epsilon)
    else:
        return argmin(f, m1, hi, epsilon)

############################################################
#####################
# the functions below are extra credit
############################################################
#####################


def find_boundaries(f):
    '''
    Returns a tuple (lo,hi).
    If f is a convex function, then the minimum is guarantee
d to be between lo and hi.
    This function is useful for initializing argmin.

    HINT:
    Begin with initial values lo= -1, hi=1.
    Let mid = (lo + hi) / 2
    if f(lo) > f(mid):
        recurse with lo *= 2
    elif f(hi) < f(mid):
        recurse with hi *= 2
    else:
        you're done; return lo,hi
    '''

    def left(lo, hi):
        mid = (lo + hi) / 2
        if f(lo) > f(mid):
            return lo
        else:
            return left(lo * 2, hi)

    def right(lo, hi):
        mid = (lo + hi) / 2
        if f(hi) > f(mid):
            return hi
        else:
            return right(lo, hi * 2)
    lo = -1
    hi = 1
    new_lo = lo
    new_hi = hi
    mid = (lo + hi) / 2
    if f(lo) < f(mid):
        new_lo = left(lo * 2, hi)
    if f(hi) < f(mid):
        new_hi = right(lo, hi * 2)
    return new_lo, new_hi


def argmin_simple(f, epsilon=1e-3):
    '''
    This function is like argmin, but it internally uses the
 find_boundaries function so that
    you do not need to specify lo and hi.

    NOTE:
    There is nothing to implement for this function.
    If you implement the find_boundaries function correctly,
    then this function will work correctly too.
    '''
    lo, hi = find_boundaries(f)
    return argmin(f, lo, hi, epsilon)


if __name__ == '__main__':
    print(count_repeats(list(range(100000, -100000, -1)), 0))
