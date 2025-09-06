# This module contains functions to lazily generate student data.

# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    # Case-insensitive match on the major; yield tuples as-is
    return (student for student in student_list if student[2].lower() == major.lower())