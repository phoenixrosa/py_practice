"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when
everyone is available.

To do this, you'll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple of
integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # Meeting from 10:00 - 10:30 am
(6, 9)  # Meeting from 12:00 - 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time
ranges. Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the
function to work even for very large numbers, like Unix timestamps. In any case, the spirit of the challenge is to
merge meetings where start_time and end_time don't have an upper bound.
"""


def merge_ranges_draft(list_of_meeting_ranges):
    # brute force = O(n^2) time and O(n) space
    # might have errors, does not ensure merged meeting times
    # some merged meetings need to merge FURTHER with merged meetings
    # ex: fails on sample_set5
    condensed_ranges = []
    current_time = 0
    last_end_time = 0
    for meeting_tuple in list_of_meeting_ranges:
        added_tuple = False
        for i in xrange(len(condensed_ranges)):
            a_check = False
            if meeting_tuple[0] <= condensed_ranges[i][0] <= meeting_tuple[1] :
                condensed_ranges[i] = (meeting_tuple[0], condensed_ranges[i][1])
                a_check = True
                added_tuple = True

            elif condensed_ranges[i][0] <= meeting_tuple[0] <= condensed_ranges[i][1]:
                a_check = True
                added_tuple = True

            if a_check and meeting_tuple[1] > condensed_ranges[i][1]:
                condensed_ranges[i] = (condensed_ranges[i][0], meeting_tuple[1])

        if not added_tuple:
            condensed_ranges.append(tuple)

    return condensed_ranges


def sort(things):
    # practice merge sort
    # top-down?

    return []


def merge_ranges(list_of_meeting_ranges):
    # sort input first
    # then merge
    # O(n log n) time and O(n) space
    if len(list_of_meeting_ranges) < 1:
        raise IndexError("should input at least 1 meeting")
    sorted_ranges = sort(list_of_meeting_ranges)
    condensed_ranges = [sorted_ranges[0]]
    i = 0
    for start_time, end_time in sorted_ranges[1:]:
        # also check to merge previous meeting with before??
        # greedy algorithm

        overlap = False
        if start_time <= condensed_ranges[i][0] <= end_time:
            # tuple overlaps first of condensed_range
            # tuple is earlier, update condensed_range
            condensed_ranges[i] = (start_time, condensed_ranges[i][1])
            overlap = True
        elif condensed_ranges[i][0] <= start_time <= condensed_ranges[i][1]:
            # condensed_range overlaps first of tuple
            # condensed is earlier, tuple merges within
            # do nothing
            overlap = True
        if overlap and end_time > condensed_ranges[i][1]:
            # tuple overlaps and is longer than condensed_range
            # update condensed_range
            condensed_ranges[i] = (condensed_ranges[i][0], end_time)
        if not overlap:
            # since input was sorted, this merged_range is done?
            # start next merged_range with tuple
            condensed_ranges.append((start_time, end_time))
            i += 1

    return condensed_ranges


sample_set1 = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
sample_set2 = [(1, 2), (2, 3)]
sample_set3 = [(1, 5), (2, 3)]
sample_set4 = [(1, 10), (2, 6), (3, 5), (7, 9)]
sample_set5 = [(1, 5), (2, 3), (3, 6), (10, 15), (14, 17), (10, 16), (6, 10)]

print merge_ranges_draft(sample_set5)



