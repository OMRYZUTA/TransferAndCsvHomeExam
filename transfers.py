
# A are integers representing transaction amounts like 2,3
# D are of dates
def solution(A, D):
    transferCalculator = TransferCalculator()
    transferCalculator.calcualte_amount(A, D)
    return transferCalculator.get_total_balance()


class TransferCalculator:
    def __init__(self):
        self.yearly_fee = -60
        self.total_balance = 0

    def get_total_balance(self):
        return self.total_balance + self.yearly_fee

    def calcualte_amount(self, transfers, dates):
        current_month = (dates[0])[5:7]
        self.handle_transfers_since_current_month(transfers, dates, current_month)

    def handle_transfers_since_current_month(self, transfers, dates, current_month):
        payment_in_month = 0
        num_of_payments = 0
        for transfer_date_tuple in zip(transfers, dates):
            if (transfer_date_tuple[1])[5:7] != current_month:
                current_month = (transfer_date_tuple[1])[5:7]
                payment_in_month = 0
            if(transfer_date_tuple[0] < 0):
                payment_in_month += transfer_date_tuple[0]
                num_of_payments += 1
            if num_of_payments >= 3 and payment_in_month <= -100:
                self.yearly_fee += 5
            self.total_balance += transfer_date_tuple[0]
