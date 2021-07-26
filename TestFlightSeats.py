import unittest
from flight_seats import check_vacancy_in_sub_row, get_num_families_in_row, solution


class TestFlightSeats(unittest.TestCase):

    def test_vacancy_in_missing_sub_row(self):
        sub_row = 'ABC'
        row = '1'
        not_vacancy_string = '1B 2C 3E 4B 4C 4D 4J'
        result = check_vacancy_in_sub_row(sub_row, row, not_vacancy_string, 2)
        self.assertFalse(result)

    def test_vacancy_in_vacant_sub_row(self):
        sub_row = 'DEFG'
        row = '1'
        not_vacancy_string = '1B2C3E4B4C4D4J'
        result = check_vacancy_in_sub_row(sub_row, row, not_vacancy_string, 2)
        self.assertTrue(result)

    def test_get_num_families_in_row(self):
        row_num = '1'
        not_vacancy_string = ''
        result = get_num_families_in_row(row_num, not_vacancy_string)
        self.assertEqual(result, 2)

    def test_get_num_families_in_busy_row(self):
        row_num = '1'
        not_vacancy_string = '1A 1B 1C 1D 1E 1F 1G 1H 1J 1K'
        result = get_num_families_in_row(row_num, not_vacancy_string)
        self.assertEqual(result, 0)

    def test_codility_test_(self):
        row_num=2
        occupy= '1A 2F 1C'
        result = solution(row_num, occupy)
        self.assertEqual(result,2)
if __name__ == '__main__':
    unittest.main()
