print("Welcome to bank PHP")
haveAccount = input("Do you have an account with us: 1 (yes) 2(no) \n")

if (haveAccount == 1):
    name = input('what is your name? \n')
name = input('what is your name? \n')
allowedUsers = ('Anu', 'Joy', 'Tobi')
allowedPassword = ['PasswordAnu', 'PasswordJoy', 'PasswordTobi']
allowedAmount = [5000, 10000, 15000, 2000]
currentBalance = 50000
complain = ['yes', 'no']

if(name in allowedUsers):
    password = input('your password \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('welcome %s' % name)
        print('these are avaliable options')
        print('1, Withdrawal')
        print('2, Cash Deposit')
        print('3, Complain')

        selectedOption = int(input('please select an option \n'))

        print(selectedOption == 1)

        if(selectedOption == 1):
            allowedAmount = (input('How much will you like to withdraw? \n'))

            print('take your cash')

        elif(selectedOption == 2):
            allowedAmount = (input('How much would you like to deposit?\n'))
            print('your Balance is')
            print(currentBalance - allowedAmount)

        elif(selectedOption == 3):
            complain = (input(' will you like to report an issue? \n'))

            print('Thank you for contacting us')
else:
    print('invalid option selected, please try again')
    
        else:
            print('name not found, please try again')
else:
    print("incorrect password, please try again")