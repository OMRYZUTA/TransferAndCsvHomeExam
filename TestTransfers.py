import unittest
from transfers import TransferCalculator


class TestTransfer(unittest.TestCase):
    def test_fee_amount_for_year_is_60(self):
        transfer_calculator = TransferCalculator()
        self.assertEqual(transfer_calculator.get_total_balance(), -60)

    def test_calculate_monthly_fee_in_month_is_reduced(self):
        transfer_calculator = TransferCalculator()

        transfer_calculator.calcualte_amount(
            [100, 100, 100], ['2020-12-31', '2020-12-22', '2020-12-03'])
        self.assertEqual(transfer_calculator.get_total_balance(), 240)

    def test_codility(self):
        transfer_calculator = TransferCalculator()
        transfer_calculator.calcualte_amount([180, -50, -25, -25], ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-31'])
        self.assertEqual(transfer_calculator.get_total_balance(),25)

if __name__ == '__main__':
    unittest.main()
