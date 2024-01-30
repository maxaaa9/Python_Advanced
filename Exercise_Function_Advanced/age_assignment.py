def age_assignment(*names, **kvp):
    result = []

    for name in names:
        if name[0] in kvp.keys():
            result.append(f"{name} is {kvp[name[0]]} years old.")

    return "\n".join(sorted(result, key=lambda x: x[0]))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))