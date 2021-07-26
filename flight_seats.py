H_VALUE = 72
TWO_CONCECUTIVE_SEATS =2
FOUR_CONCECUTIVE_SEATS =4

def solution(N, S):
    families_num = 0
    for i in range(1, N+1):
        families_num += get_num_families_in_row(str(i), S)
    return families_num


def check_if_sub_row_is_seatable(sub_row, num_of_seats):
    result = False
    consecutive_vacant_seats = 0
    if len(sub_row) >= num_of_seats:
        previous_seat_value = ord(sub_row[0])
        consecutive_vacant_seats += 1
        for i in range(1, len(sub_row)):
            if(previous_seat_value == H_VALUE):
                previous_seat_value += 1
            if ord(sub_row[i]) == previous_seat_value+1:
                consecutive_vacant_seats += 1
                previous_seat_value = ord(sub_row[i])
            else:
                consecutive_vacant_seats = 0
        if consecutive_vacant_seats >= num_of_seats:
            result = True
    return result


def check_vacancy_in_sub_row(sub_row, row, occupy_list, num_of_seats):
    index_search_start = 0
    row_index_in_string = occupy_list.find(row, index_search_start)
    while(row_index_in_string != -1):
        if occupy_list[row_index_in_string+1] in sub_row:
            sub_row = sub_row.replace(
                occupy_list[row_index_in_string+1], '')
        row_index_in_string = occupy_list.find(row, row_index_in_string+1)
    result = check_if_sub_row_is_seatable(sub_row, num_of_seats)
    return result
    # N is number of rows S is string of occupy_list


def get_num_families_in_row(row_num, occupy_string):
    num_of_families = 0
    if check_if_two_families(row_num, occupy_string):
        num_of_families += 2
    elif check_if_one_family(row_num, occupy_string):
        num_of_families += 1
    return num_of_families


def check_if_two_families(row_num, occupy_string):
    return(check_vacancy_in_sub_row('BC', row_num, occupy_string, 2) and check_vacancy_in_sub_row('HJ', row_num, occupy_string, 2) and check_vacancy_in_sub_row('DEFG', row_num, occupy_string, 4))


def check_if_one_family(row_num, occupy_string):
    return(check_vacancy_in_sub_row('BC', row_num, occupy_string, 2) and check_vacancy_in_sub_row('DE', row_num, occupy_string, 2) or check_vacancy_in_sub_row('DEFG', row_num, occupy_string, 4) or check_vacancy_in_sub_row('FG', row_num, occupy_string, 2) and check_vacancy_in_sub_row('HJ', row_num, occupy_string, 2))
