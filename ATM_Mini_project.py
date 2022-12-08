'''
Q> You task is to replicate the working of ATM for a single user, let's say, Mr. John, who has already successfully 
 logged into his account on the ATM Machine, now, we will program the next steps he may want to perform.
Like display his name and cash available in his savings account
Withdraw cash and display the status of the cash balance.

Deposit cash and display the status of the cash balance. (Your task is to design and implement the ATM functionality by taking care of all constraints, for
example if minimum cash available is less than 5000 then system will display low balance)
'''


name='John Price'
def atm(totamt):
    print('>                 __ >> Login succesfull << __                <')
    print()
    print('>                 __ >> Welcome Mr. John << __                <')
    print()
    print('>                 __ >>    Name-->  '+name+' << __                <')

    print('>                 __ >>    Balance ammount -> ₹ ',totamt,' << __                <')
    print()
    print('>                 __ >> -- Enter your choice -- << __                <')
    print()
    print('>                 __ >> Press 1 to Deposit Cash << __                <')
    print('>                 __ >> Press 2 to Withdraw Cash << __                <')
    print('>                 __ >> Or press 99 to Exit ATM services << __                <')
    print()
    while True:
        cho=int(input('     Input your choice =         '))
        if cho==1 or cho==2:
            print('>                 __ >> Your Choice is --',cho,' << __                <')
            break
        elif cho==99:
            print('     You has Escaped your ATM services     ')
            break
        else:
            print('!!!!!     You have entered an invalid choice      !!!!!')

    match cho :
        case 2 :
            withdraw(totamt)
        case 1 :
            deposit(totamt)
        
    print(" ** _THANK YOU FOR USING OUR ATM_ ** ",'\n'*2)
            




def withdraw(totamt):
    amt=int(input('    Enter the amount that you want to withdraw from your Account --   '))
    
    if amt>=totamt:
         print('     __ >> Your withdrawal amount is greater than equal your available balance !!!!!')
    else:
        totamt=totamt-amt
        print('\n', f"--  ₹{amt}   -- withdrawn from your Account")
        balance(totamt)   




def deposit(totamt):
    amt=int(input('    Enter the amount that you want to Deposit to your Account --   '))
    totamt= totamt +amt
    print('\n', f"--  ₹{amt}   -- added to your Account")
    balance(totamt)


#def low():


def balance(totamt):
    print(f" Your current balance is ₹{totamt} ")
    if(totamt<=5000):
        print(" !!!!! LOW BALANCE !!!!! ")

    
totamt=65000
atm(totamt)