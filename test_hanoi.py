from hanoi import Tower
from hanoi import solve
from nose.tools import assert_equals
from nose.tools import assert_raises

def test_solve_four_discs():
    result = solve(4)
    # Largest (highest numbered) disc should be on the top of the stack
    assert_equals(range(3, -1, -1), result[2].discs)

def test_solve_three_discs():
    result = solve(3)
    assert_equals(range(2, -1, -1), result[2].discs)
    
def test_solve_two_discs():
    result = solve(2)
    assert_equals([1, 0], result[2].discs)

def test_solve_one_disc():
    pass

def test_solve_no_discs():
    pass

# Skipping tests for invalid disc parameters

def move_discs_almost_solved():
    pass

def test_add_larger_disc():
    pass

# This should never happen, because there is only one of each disc
def test_add_same_disc():
    pass

def test_add_smaller_disc():
    pass

def test_move_discs_none_left():
    pass

def test_move_discs_last_one():
    pass

def test_move_discs_same_start_end():
    pass

def test_move_disc_same_start_temp():
    pass




