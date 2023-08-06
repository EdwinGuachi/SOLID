import MyBankApi
import PaymentProcessor

class MyBankPaymentProcessor(PaymentProcessor):
    def __init__(self, myBankApi: MyBankApi):
        self.myBankApi = myBankApi

    def pay(self):
        self.myBankApi.charge()