# This module contains functions to process student data.

def format_student_data(student):
    """
    Return a formatted string:
    "ID: <id> | Name: <name> | Major: <major>"
    """
    sid, name, major = student
    return f"ID: {sid} | Name: {name} | Major: {major}"

def display_students(student_list):
    """
    Print every student's details using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))