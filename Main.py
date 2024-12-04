import datetime
import csv
import pandas as pd
class Transaction: 

    def __init__(self, idnum: int, 
                 amount: float, 
                 date: datetime.datetime, 
                 category: str, 
                 description: str, 
                 account_id: int):
        
        
        self.idnum = idnum
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description
        self.account_id = account_id
        self.data_file = "TransactionTracker/Transaction.csv"

        

        
        if amount <= 0:
            raise ValueError("Сума транзакції має бути додатньою")
        
        if not isinstance(date, datetime.datetime):
            raise TypeError("Невірний формат дати")
        
        if not category:
            raise ValueError("Категорія не може бути порожньою")
        

    def create_transaction(self):
        formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        transaction = (self.idnum, self.amount, formatted_date, self.category, self.description, self.account_id)
        print(f"Will be added to a database: {transaction}")
        return transaction


    def append_to_csv(self):
        try:
            transaction = self.create_transaction()
            with open(self.data_file, 'a', newline='') as CSVdata:
                writer = csv.writer(CSVdata)
                writer.writerow(transaction)
        except Exception as e:
            print(f"Error writing to file: {e}")

    def show_transaction():
        try: 
            data = pd.read_csv("TransactionTracker/Transaction.csv")
            print(data.to_csv())
        except Exception as e:
            print(f"Error writing to file: {e}")
        

def main():
    while True:
        option = int(input("""
        Choose an option:
        1. Create transaction
        2. Show history of transactions 
        3. 
        4. 
        5. 
        """))
        if option == 1:
            idnum = int(input("ID: "))
            amount = float(input("Amount: "))
            category = str(input("Category: "))
            description = str(input("Descripton: "))
            account_id = int(input("Account ID: "))

            transaction = Transaction(
            idnum=idnum,
            amount=amount,
            date= datetime.datetime.now(),
            category=category,
            description=description,
            account_id=account_id
            )

            transaction.append_to_csv()

        elif option == 2:
            Transaction.show_transaction()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            break



if __name__ == "__main__":
    main()