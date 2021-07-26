
# S is table C is
def solution(S, C):
    scheme = parse_scheme_from_string(S)
    column = get_num_of_column_from_scheme(scheme, C)
    rows = get_rows_from_string(S)
    ints_list = get_ints_list_from_table(rows, column)
    return get_max_from_ints_list(ints_list)


def get_rows_from_string(string):
    all_table = string.split('\n')
    return all_table[1:]


def get_num_of_column_from_scheme(scheme, column):
    columns = scheme.split(',')
    result = -1
    for i in range(len(columns)):
        if columns[i] == column:
            result = i
    return result


def parse_scheme_from_string(string):
    rows = string.split('\n')
    return rows[0]


def get_ints_list_from_table(rows_array, column_num):
    ints_list = []
    for row in rows_array:
        values = row.split(',')
        ints_list.append(int(values[column_num]))
    return ints_list


def get_max_from_ints_list(ints_list):
    return max(ints_list)
