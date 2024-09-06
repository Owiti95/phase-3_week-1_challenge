def sort_by_age(users):
    # Sort the list of tuples by the second element (age)
    return sorted(users, key=lambda user: user[1])

# how it would work
users = [("Hannington", 20), ("Owiti", 21), ("Omondi", 22)]
sorted_users = sort_by_age(users)
print(sorted_users)
