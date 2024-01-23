from timeit import repeat

def run_time_algorithm(function):
    setup = 'from __main__ import {}'.format(function)
    stmt = function
    result = repeat(setup = setup, stmt = stmt, repeat = 10, number = 1000)
    print(min(result))
    
