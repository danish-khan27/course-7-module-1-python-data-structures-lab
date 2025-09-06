# This module contains functions for filtering student data.

def filter_students_by_major(student_list, major):
    """
    Return a list of students whose major matches (case-insensitive).
    """
    return [s for s in student_list if s[2].lower() == major.lower()]

