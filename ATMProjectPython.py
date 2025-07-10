import time
password = 1234
Balance = 10000
print("Welcome to ATM")
print("Insert the card")
print("1.yes\n 2.no")
choice = int(input())
if choice == 1:
    print("Select Language")
    print("1.English\n 2.Telugu")
    lang = int(input())
    if lang == 1 :
        print("enter your pin")
        pin = int(input())
        if pin == password:
            print("select your option")
            print("1.Balance query\n 2.Withdrawl")
            option = int(input())
            if option == 1 :
                print("Your available balance is", Balance)
            elif option == 2 :
                print("Enter the amount")
                amount = int(input())
                print("Transaction is processing....")
                time.sleep(4)
                if amount <= Balance:
                    if amount % 100 == 0:
                        print("Please collect your cash!")
                        Balance = Balance - amount
                        time.sleep(3)
                    else:
                        print("ATM can't accept")
                        time.sleep(3)
                else:
                    print("Insufficient balance")
                    time.sleep(3)
                print("Do you want to check your Current Balance")
                print("1.yes\n 2.No\n ")
                choice1 = int(input())
                if choice1 == 1:
                    if amount > Balance:
                        print("Your available balance is" , Balance)
                        print("Thank you, Visit again")
                    else:
                        print("your available balance is", Balance )
                else:
                    print("Thank you, Visit again")
            else:
                print("Select the correct option")
        else:
            print("Please enter correct pin")
    else:
        print("please select English")
else:
    print("insert your card properly")





