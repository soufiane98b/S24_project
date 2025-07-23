def compute_day(list_lantern_fish):
    nb_new_fish = 0
    for i in range(len(list_lantern_fish)):
        list_lantern_fish[i] = list_lantern_fish[i] - 1
        if list_lantern_fish[i] == -1:
            list_lantern_fish[i] = 6
            nb_new_fish += 1

    return list_lantern_fish + [8] * nb_new_fish


def compute_n_days(list_lantern_fish, days):
    for _ in range(days):
        list_lantern_fish = compute_day(list_lantern_fish)

    return list_lantern_fish


list_lantern_fish = [1, 1, 3, 5, 3, 1, 1, 4, 1, 1, 5, 2, 4, 3, 1, 1, 3, 1, 1, 5, 5, 1, 3, 2, 5, 4, 1, 1, 5, 1, 4, 2, 1,
                     4, 2, 1, 4, 4, 1, 5, 1, 4, 4, 1, 1, 5, 1, 5, 1, 5, 1, 1, 1, 5, 1, 2, 5, 1, 1, 3, 2, 2, 2, 1, 4, 1,
                     1, 2, 4, 1, 3, 1, 2, 1, 3, 5, 2, 3, 5, 1, 1, 4, 3, 3, 5, 1, 5, 3, 1, 2, 3, 4, 1, 1, 5, 4, 1, 3, 4,
                     4, 1, 2, 4, 4, 1, 1, 3, 5, 3, 1, 2, 2, 5, 1, 4, 1, 3, 3, 3, 3, 1, 1, 2, 1, 5, 3, 4, 5, 1, 5, 2, 5,
                     3, 2, 1, 4, 2, 1, 1, 1, 4, 1, 2, 1, 2, 2, 4, 5, 5, 5, 4, 1, 4, 1, 4, 2, 3, 2, 3, 1, 1, 2, 3, 1, 1,
                     1, 5, 2, 2, 5, 3, 1, 4, 1, 2, 1, 1, 5, 3, 1, 4, 5, 1, 4, 2, 1, 1, 5, 1, 5, 4, 1, 5, 5, 2, 3, 1, 3,
                     5, 1, 1, 1, 1, 3, 1, 1, 4, 1, 5, 2, 1, 1, 3, 5, 1, 1, 4, 2, 1, 2, 5, 2, 5, 1, 1, 1, 2, 3, 5, 5, 1,
                     4, 3, 2, 2, 3, 2, 1, 1, 4, 1, 3, 5, 2, 3, 1, 1, 5, 1, 3, 5, 1, 1, 5, 5, 3, 1, 3, 3, 1, 2, 3, 1, 5,
                     1, 3, 2, 1, 3, 1, 1, 2, 3, 5, 3, 5, 5, 4, 3, 1, 5, 1, 1, 2, 3, 2, 2, 1, 1, 2, 1, 4, 1, 2, 3, 3, 3,
                     1, 3, 5]

print(len(compute_n_days(list_lantern_fish, 80)))
# Answer : 361169
