from perms_recurse import perms
from perms_recurse import perms_partial
from nose.tools import assert_equals

def test_perms_empty():
    assert_equals(perms(""), set())

def test_perms_single():
    assert_equals(perms("a"), set("a"))

def test_perms_two():
    assert_equals(perms("ab"), set(["ab", "ba"]))

def test_perms_three():
    assert_equals(perms("abc"), set(["abc", "acb", "bac", "bca", "cab", "cba"]))

def test_perms_duplicates():
    assert_equals(perms("abb"), set(["abb", "bab", "bba"]))

def test_perms_partial_empty():
    assert_equals(perms_partial(""), [""])

def test_perms_partial_single():
    assert_equals(perms_partial("a"), ["a"])

def test_perms_partial_two():
    assert_equals(perms_partial("ab"), ["ab", "ba"])

def test_perms_partial_three():
    # Use sets to avoid mismatches due to ordering
    expected = set(["abc", "acb", "bac", "bca", "cab", "cba"])
    assert_equals(set(perms_partial("abc")), expected)

# This non-set version should have multiple entries for each duplicate
def test_perms_partial_duplicates():
    assert_equals(perms_partial("bb"), ["bb", "bb"])
