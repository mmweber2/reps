def permute(s):
    if len(s) <= 1:
        return set(s)
    perms = set()
    for i in xrange(len(s)):
        for perm in permute(s[:i] + s[i+1:]):
            perms.add(s[i] + perm)
    return perms

def permute(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i in xrange(len(s)):
        current = s[i]
        for perm in permute(s[:i] + s[i+1:]):
            perms.append(current + perm)
    return perms

