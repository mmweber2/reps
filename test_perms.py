from perms_recurse import perms
from nose.tools import assert_equals

def test_empty():
    assert_equals(perms(""), set())

def test_single():
    assert_equals(perms("a"), set("a"))

def test_two():
    assert_equals(perms("ab"), set(["ab", "ba"]))

def test_three():
    assert_equals(perms("abc"), set(["abc", "acb", "bac", "bca", "cab", "cba"]))

def test_duplicates():
    assert_equals(perms("abb"), set(["abb", "bab", "bba"]))

