# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique majors from the student list.
    """
    return {s[2] for s in student_list}