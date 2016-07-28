from perms_recurse import perms
from perms_recurse import perms_partial
from perms_recurse import perms_partial2
from perms_recurse import perms
from nose.tools import assert_equals
from itertools import permutations

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
    # Sort to avoid mismatches due to ordering
    expected = sorted(["abc", "acb", "bac", "bca", "cab", "cba"])
    assert_equals(sorted(perms_partial("abc")), expected)

def test_perms_partial_four():
    expected = ["".join(x) for x in permutations("6789")]
    assert_equals(sorted(perms_partial("6789")), expected)

# This non-set version should have multiple entries for each duplicate
def test_perms_partial2_duplicates():
    assert_equals(perms_partial2("bb"), ["bb", "bb"])

# Alternate (more standard) version
def test_perms_partial2_empty():
    assert_equals(perms_partial2(""), [""])

def test_perms_partial2_single():
    assert_equals(perms_partial2("a"), ["a"])

def test_perms_partial2_two():
    assert_equals(sorted(perms_partial2("ab")), ["ab", "ba"])

def test_perms_partial2_three():
    # Sort to avoid mismatches due to ordering
    expected = sorted(["abc", "acb", "bac", "bca", "cab", "cba"])
    assert_equals(sorted(perms_partial2("abc")), expected)

def test_perms_partial2_four():
    expected = ["".join(x) for x in permutations("6789")]
    assert_equals(sorted(perms_partial2("6789")), expected)

# This non-set version should have multiple entries for each duplicate
def test_perms_partial2_duplicates():
    assert_equals(perms_partial2("bb"), ["bb", "bb"])
