from sys import path
path.append('..\\')
from model.fakedb import portfolio_list, transactions_list

class Portfolio:

    def __init__(self, id_portfolio, id_user, transactions = []):
        self.id_portfolio = id_portfolio
        self.id_user = id_user
        self.trasactions = transactions

    def __str__(self):
        return f"Portfolio id: {self.id_portfolio}, owned by user id: {self.id_user}"

    @classmethod
    def get_portfolio_from_db(self, id_portfolio): #Simula buscar el portfolio en la BD
        for portfolio in portfolio_list:
            if portfolio["id_portfolio"] == id_portfolio:
                id_portfolio = portfolio["id_portfolio"]
                id_user = portfolio["id_user"]
                transactions = []
                for transaction in transactions_list: 
                    if transaction["id_portfolio2"] == id_portfolio: #Esto lo haría un JOIN, trayendo las operaciones de la otra tabla
                        transactions.append(transaction)
                return (Portfolio(id_portfolio, id_user, transactions)).__dict__
        
        raise Exception ("Portfolio not found")   


    @classmethod
    def insert_portfolio_to_db(self, id_portfolio, id_user): #Simula insertar Portfolio en la BD
        portfolio_list.append(Portfolio(id_portfolio, id_user).__dict__)


