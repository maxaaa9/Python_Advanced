def fill_the_box(height, length, width, *nums):
    total_space = height * length * width
    for cube in nums:
        if cube == "Finish":
            break
        total_space -= cube

    if total_space >= 0:
        return f"There is free space in the box. You could put {total_space} more cubes."
    return f"No more free space! You have {abs(total_space)} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

