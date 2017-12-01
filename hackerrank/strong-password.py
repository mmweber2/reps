# HackerRank problem Strong Password
# https://www.hackerrank.com/contests/hourrank-24/challenges/strong-password

def minimumNumber(password):
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")
    has_num = False
    has_lower = False
    has_upper = False
    has_special = False
    for c in password:
        if c in numbers:
            has_num = True
        elif c in lower_case:
            has_lower = True
        elif c in upper_case:
            has_upper = True
        elif c in special_characters:
            has_special = True
    must_add = 0
    for check in (has_num, has_lower, has_upper, has_special):
        if not check:
            must_add += 1
    if len(password) + must_add >= 6:
        return must_add
    return 6 - len(password)
   
if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    print minimumNumber(password)
