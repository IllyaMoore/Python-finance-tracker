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
        self.data_file = ["TransactionTracker/Transaction.csv", "TransactionTracker/income.csv"]

        if amount <= 0:
            raise ValueError("amount of transaction can`t be a negative number")
        
        if not category:
            raise ValueError("category can`t be empty")


    def create_transaction(self):
        formatted_date = self.date.strftime("%Y-%m-%d %H:%M:%S")
        transaction = (self.idnum, self.amount, formatted_date, self.category, self.description, self.account_id)
        print(f"Will be added to a database: {transaction}")
        return transaction


    def append_to_csv(self, choise):
        try:
            transaction = self.create_transaction()
            if choise == 1:
                with open(self.data_file[0], 'a', newline='') as CSVdata:
                    writer = csv.writer(CSVdata)
                    writer.writerow(transaction)
            if choise == 2:
                with open(self.data_file[1], 'a', newline='') as CSVdata:
                    writer = csv.writer(CSVdata)
                    writer.writerow(transaction)
                    
        except Exception as e:
            print(f"Error writing to file: {e}")

    def show_transaction(choise):
        try: 
            if choise == 1:
                data = pd.read_csv('TransactionTracker/Transaction.csv')
                print(data.to_csv())
            if choise == 2:
                data = pd.read_csv('TransactionTracker/income.csv')
                print(data.to_csv())
        except Exception as e:
            print(f"Error reading the file: {e}")
        

class Statistics:
    
    data_file_transaction = "TransactionTracker/Transaction.csv"
    data_file_income = "TransactionTracker/income.csv"

    def read_statistics_file(data_file_transaction=data_file_transaction, data_file_income=data_file_income):
        data_transaction = pd.read_csv(data_file_transaction)
        data_file_income = pd.read_csv(data_file_income)
        return (data_transaction, data_file_income)

    def get_amount_stat():    
        data = Statistics.read_statistics_file()
        data_transaction, data_file_income = data
        amount_meen_transaction = data_transaction['amount'].mean()
        amount_max_transaction = data_transaction['amount'].max()
        amount_min_transaction = data_transaction['amount'].min()
        
        data_sum_income = data_file_income['amount'].sum()
        data_sum_transaction = data_transaction['amount'].sum()

        category_max = data_transaction.loc[data_transaction['amount'].idxmax(), 'category']
        category_min = data_transaction.loc[data_transaction['amount'].idxmin(), 'category']
        date_max = data_transaction.loc[data_transaction['amount'].idxmax(), 'date']
        date_min = data_transaction.loc[data_transaction['amount'].idxmin(), 'date']
        return (amount_meen_transaction, 'N/A'), (amount_max_transaction, category_max, date_max), (amount_min_transaction, category_min, date_min), (data_sum_income, data_sum_transaction)

    def show_stats():
        stats = Statistics.get_amount_stat()
        amount_meen_transaction, amount_max_transaction, amount_min_transaction, data_max_income_transaction = stats
        budget_left = data_max_income_transaction[0] - data_max_income_transaction[1]

        print(f"\nTotal Income: {data_max_income_transaction[0]}")
        print(f"\nThe largest purchase amount: {amount_max_transaction[0]}\n In category: {amount_max_transaction[1]}\n On date: {amount_max_transaction[2]} \n")
        print(f"The lowest purchase amount: {amount_min_transaction[0]}\n In category: {amount_min_transaction[1]}\n On date {amount_min_transaction[2]} \n")
        print(f"Average purchase amount: {amount_meen_transaction[0]}\n In category: {amount_meen_transaction[1]}")
        print(f"Budget left: {budget_left}")
def main():
    def get_category():
        print('1.Needs')
        print('2.Housing')
        print('3.Clothing')
        print('4.Transportation')
        print('5.Health and Wellness')
        print('6.Education')

        choice = int(input())
        category_name = ''
        if choice == 1:
            category_name = 'Needs'
        elif choice == 2:
            category_name = 'Housing'
        elif choice == 3:
            category_name = 'Clothing'
        elif choice == 4:
            category_name = 'Transportation'
        elif choice == 5:
            category_name = 'Health and Wellness'
        elif choice == 6:
            category_name = 'Education'
        else:
            print("wrong input")
        return category_name
    


    while True:
        option = int(input("""                           
        Choose an option:
        1. Create transaction
        2. Show history of transactions 
        3. Show avarage transaction info
        4. 
        5. Exit
        """))

        if option == 1:
            print("append to a Incame, or transaction?\n1.Transaction\n2.Incame")
            choise = int(input("Make a choise:"))
            idnum = int(input("ID: "))
            amount = float(input("Amount: "))
            category = get_category()
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

            transaction.append_to_csv(choise=choise)

        elif option == 2:
            choise = int(input("Make a choise:\n1.Transaction\n2.Income\n"))
            Transaction.show_transaction(choise=choise)
        elif option == 3:
            Statistics.show_stats()
        elif option == 4:
            pass
        elif option == 5:
            break



if __name__ == "__main__":
    main()