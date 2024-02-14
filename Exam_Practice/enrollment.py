def gather_credits(needed_credit, *data):
    collected_credits = 0
    my_courses = []
    for course, credit in data:
        if collected_credits >= needed_credit:
            break
        if course not in my_courses:
            my_courses.append(course)
            collected_credits += credit
    return_string = ""
    if collected_credits >= needed_credit:
        return_string += f"Enrollment finished! Maximum credits: {collected_credits}.\n" \
                         f"Courses: {', '.join(sorted(my_courses))}"
    else:
        difference = needed_credit - collected_credits
        return_string += f"You need to enroll in more courses! You have to gather {difference} credits more."

    return return_string


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))