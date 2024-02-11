def softuni_students(*data, **student_info):
    my_print = ""
    valid_students = {}
    invalid_students = []
    for id_num, username in data:
        if id_num in student_info.keys():
            valid_students[username] = student_info[id_num]
        else:
            invalid_students.append(username)

    valid_students = dict(sorted(valid_students.items(), key=lambda x: x[0]))
    for user, course in valid_students.items():
        my_print += f"*** A student with the username {user} " \
                    f"has successfully finished the course {course}!\n"

    if invalid_students:
        my_print += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return my_print



