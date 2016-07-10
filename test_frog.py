from frog import frog
from nose.tools import assert_equals

def test_zero_steps():
    assert_equals(frog(0, 1), 1)

def test_negative_steps():
    assert_equals(frog(-1, 1), 0)

def test_zero_jumps():
    assert_equals(frog(5, 0), 0)

def test_negative_jumps():
    assert_equals(frog(5, -1), 0)

def test_one_step_one_jump():
    assert_equals(frog(1, 1), 1)

def test_jump_bigger_than_step():
    assert_equals(frog(1, 2), 1)

def test_two_steps_one_jump():
    assert_equals(frog(2, 1), 1)

def test_two_steps_two_jumps():
    assert_equals(frog(2, 2), 2)

def test_three_steps_one_jump():
    assert_equals(frog(3, 1), 1)

def test_three_steps_two_jumps():
    assert_equals(frog(3, 2), 3)

