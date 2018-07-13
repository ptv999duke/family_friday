import random
import queue

MAX_GROUP_SIZE = 5
MIN_GROUP_SIZE = 3

# Map<tea_num, list(people)>
def arrange_family_friday(teams):

    # num_of_groups = len(people)/5
    # remainder = len(people) % 5
    # if remainder < MIN_GROUP_SIZE:
        # breakup(last_group_of_5) -> 3, 2 -> 3, 2 + 1 -> 3, 3
    if teams is None:
        raise ValueError("Cannot pass null people group")

    final_grouping = []
    current_group = []

    team_p_q = queue.PriorityQueue()
    for team_num in teams:
        team_p_q.put((len(teams[team_num]), team_num))

    temp_team_holdings = []
    while team_p_q.qsize() > 0:
        team_info = team_p_q.get()
        team_available_count = team_info[0]
        team_num = team_info[1]
        curr_person_index = random.randint(0, team_available_count - 1)
        team_members = teams[team_num]
        curr_person = team_members[curr_person_index]

        current_group.append(curr_person)
        teams[curr_person_index] = teams[team_available_count - 1]
        teams[team_available_count - 1] = curr_person_index
        new_team_count = team_available_count - 1
        if new_team_count <= 0:
            continue

        temp_team_holdings.append((new_team_count, team_num))
        if team_p_q.qsize() <= 0 and len(temp_team_holdings) > 0:
            for held_team_info in temp_team_holdings:
                team_p_q.put(held_team_info)
            temp_team_holdings.clear()

        if len(current_group) >= MAX_GROUP_SIZE or team_p_q.qsize() <= 0 and len(temp_team_holdings) <= 0:
            final_grouping.append(current_group)
            current_group = []

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

print(arrange_family_friday(
    {
        0: [1, 2, 3, 4],
        1: [5, 6, 7],
        2: [8]
    }
))