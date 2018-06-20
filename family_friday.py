import random

MAX_GROUP_SIZE = 5
MIN_GROUP_SIZE = 3

def arrange_family_friday(people):

    # num_of_groups = len(people)/5
    # remainder = len(people) % 5
    # if remainder < MIN_GROUP_SIZE:
        # breakup(last_group_of_5) -> 3, 2 -> 3, 2 + 1 -> 3, 3
    if people is None:
        raise ValueError("Cannot pass null people group")
    if len(people) < 3:
        return [people]

    final_grouping = []

    current_group = []
    for i in range(len(people) - 1, -1, -1):
        temp_group = None
        curr_person_index = random.randint(0, i)
        curr_person = people[curr_person_index]
        if len(current_group) >= MAX_GROUP_SIZE:
            temp_group = current_group
            current_group = []

        current_group.append(curr_person)
        people[curr_person_index] = people[i]
        people[i] = curr_person

        if temp_group is not None:
            final_grouping.append(temp_group)
        if i == 0:
            final_grouping.append(current_group)

    if len(final_grouping[-1]) < MIN_GROUP_SIZE:
        group_to_add_to = final_grouping[-1]
        for i in range(len(final_grouping) - 2, -1, -1):
            group_to_remove_from = final_grouping[i]
            num_people_to_move = min(len(group_to_remove_from) - MIN_GROUP_SIZE, MIN_GROUP_SIZE - len(group_to_add_to))
            group_to_add_to.extend(group_to_remove_from[len(group_to_remove_from) - num_people_to_move:len(group_to_remove_from)])
            for i in range(num_people_to_move):
                group_to_remove_from.pop()
            if len(group_to_add_to) >= MIN_GROUP_SIZE:
                break

    return final_grouping