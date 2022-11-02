class Portfolio:

    def __init__(self, id_portfolio, id_user, transactions = []):
        self.id_portfolio = id_portfolio
        self.id_user = id_user
        self.transactions = transactions

    def __str__(self):

        return f"Portfolio id: {self.id_portfolio} belonging to user with id: {self.id_user}, has the folowing operations: {self.transactions}"

    def get_active_transactions(self):
        pass

    def get_closed_transactions(self):
        pass