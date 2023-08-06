import PaymentProcessor

class Store:
    def __init__(self, paymentProcessor: PaymentProcessor):
        self.paymentProcessor = paymentProcessor

    def purchase(self):
        self.paymentProcessor.charge()