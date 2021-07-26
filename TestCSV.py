import unittest
from get_max_in_column_in_CSV import get_num_of_column_from_scheme, parse_scheme_from_string, get_ints_list_from_table


class TestCSV(unittest.TestCase):
    def test_get_number_of_column(self):
        scheme = "id,name,room"
        column = 'room'
        result = get_num_of_column_from_scheme(scheme, column)
        self.assertEqual(result, 2)

    def test_parse_scheme_from_string(self):
        string = "id,name,room\n1,jack,28"
        result = parse_scheme_from_string(string)
        self.assertEqual(result, "id,name,room")

    # todo

    def test_parse_first_int_from_column(self):
        string = "id,name,room\n1,jack,28"
        column = 'room'
        ints_list = get_ints_list_from_table(["1,jack,28"], 2)
        self.assertEqual(ints_list, [28])

    def test_max_from_list(self):
        int_list =[1,4,6]
        result =max(int_list)
        self.assertEqual(result,6)

if __name__ == '__main__':
    unittest.main()
