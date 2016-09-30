# Hackerrank Lisa's Workbook problem.

def count_special(per_page, problem_counts):
    page = 1
    special_count = 0
    for chapter in xrange(len(problem_counts)):
        chapter_pages = problem_counts[chapter] / per_page
        if problem_counts[chapter] % per_page != 0:
            chapter_pages += 1
        for chapter_page in xrange(chapter_pages):
            final = min(per_page * (chapter_page + 1), problem_counts[chapter])
            problems = range(1 + (per_page * chapter_page), final + 1)
            if page in problems:
                # We cannot break early here because there could be one problem
                # per page, in which case there could be many special problems
                # in one chapter
                special_count += 1
            page += 1
    print special_count
