#Importing lib/packages
import time

#------------------------------------------------------------------------
#Global Vars
count = 0
txt1 = "Please enter your choice:"
txt2 = 'Please take your cash'
txt3 = 'Thank you!, Goodbye :)'
txt4 = 'Processing...'
txt5 = '__________________________________' # <<< Breaker
Break = False
WithdrawAmount = [50, 100, 200, 500, 1000, '* for Other Amount']
#------------------------------------------------------------------------

# The check point where the system going to check the user credential and authentication 
def DataSecurity():
  global Break
  CS = ClientServer()
  container_Cardcode=[]
  container_PinCode= []

  for i in range(len(CS.users)):
    container_Cardcode.append(CS.users[i][2][2])  
  for j in range(len(CS.users)):
    container_PinCode.append(CS.users[j][2][0])
  
  UserCode = int(input('Please enter/slide the card:\n Please press 0 to exit\n>>')) # <<< User Input 
  if (UserCode in container_Cardcode):
    print('Pass')
  elif(UserCode == 0):
    print('Please take your card')
    return 0
  else:
     # if wrong entry then go back ang ask again
    UserCode = int(input('Please enter/slide the card:\n Please press 0 to exit\n>>')) 
    

  UserPIN = int(input('Please enter PIN:'))
  if (UserPIN in container_PinCode):
    if(container_Cardcode.index(UserCode) == container_PinCode.index(UserPIN)):  # <<< position comparstion (T/F)
      # Compare UserCode index against the PINCode index. Note: the card number index and PIN number index should meet because there are belong to the same person(tuple).
      # if TRUE process
      # if FALSE run the program in loop
      while not Break:
        UserInterface()
        user = int(input('Do you want another transaction?\n [1] for Yes \n [0] for No\n '))
        if user == 1:
          continue
        else:
            break
    else:
      txt5 # << global var [Breaker]
      print("your entry doesn't match! Please try again")
      DataSecurity()
  return

# The system display interface 
def UserInterface():
    global count # <<< for counting list
    global WithdrawAmount # <<< Var to represent the list of the Withdraw Amount
    CS = ClientServer() # <<< Call ClientServer() class (User Data)
    # Display list to display and guidt he user through transactions 
    display_list = [['Checking', 'Saving'],
                    ['Withdraw', 'Deposit', 'Check Balance'],
                    ['Cash Deposit', 'Check deposit']]
    # Withdraw list contains the displaied amounts for the user
    WithdrawAmount
    # Print the welcoming sgin 
    print('Welcome to bank X\n Please choose from the options below:')
    #Display >>> 'Checking', 'Saving'
    for i in display_list[0]:
        count = count + 1
        print(count, '-', i)
    user = int(input(txt1))
    #Checking Options
    if user == 1:
        # Display >>> 'Withdraw', 'Deposit', 'Check Balance'
        for i in display_list[1]:
            count = count + 1
            print(count, '-', i)
        user = int(input(txt1))
        # Withdraw option for Checking
        if user == 3:
            for i in WithdrawAmount:
              count = count + 1
              print(i)
        user = int(input('Please enter the amount:'))
        if user == WithdrawAmount[0]:
            print(txt4)
            time.sleep(5)
            print(txt2)
            time.sleep(2)
            print('The new Balance:',CS.users[0][3].get('Checking Balance')-WithdrawAmount[0])
        elif user == WithdrawAmount[1]:
            print(txt4)
            time.sleep(5)
            print(txt2)
            time.sleep(2)
            print('The new Balance:',CS.users[0][3].get('Checking Balance')-WithdrawAmount[1])
        elif user == WithdrawAmount[2]:
            print(txt4)
            time.sleep(5)
            print(txt2)
            time.sleep(2)
            print('The new Balance:',CS.users[0][3].get('Checking Balance')-WithdrawAmount[2])

    #Saving Options
    elif user == 2:
        # Display >>> 'Withdraw', 'Deposit', 'Check Balance'
        for i in display_list[1]:
            count = count + 1
            print(count, '-', i)
        user = int(input(txt1))
        # Withdraw option for Saving
        if user == 3:
            for i in WithdrawAmount:
                print(i)
    else:
      print('Goodbye') # if the user want to exit the transaction then press on any key
    return

# Client Server contains all the clients information going to be stored and requested from
class ClientServer():
  global WithdrawAmount
  users = [
     [
    {'Name':'Rayan G.'}, #0 # <<< Genreal info
    {'Birthday':'11/10/92'}, #1 # <<< General info
    (4593, '11/25', 7987648464654654654146654654), #2 # <<< re-call for security prop. (PIN CODE , CARD EXP. , CARD SERIAL NUMBER)
    {'Checking Balance':10000, 'Saving Balance':2500}], #3 # <<< Auto update after transactions 
    [
    {'Name':'John Doe'},
    {'Birthday':'08/09/80'},
    (8258, '07/22', 3181364568465413168435418748),
    {'Checking Balance':100000, 'Saving Balance':2500}],
    [
    {'Name':'Omar Emar'},
    {'Birthday':'01/12/89'},
    (3569, '10/21', 6546469464645698654646546464),
    {'Checking Balance':100000, 'Saving Balance':2500}],
    [
    {'Name':'Jolia S.'},
    {'Birthday':'10/10/81'},
    (7562, '02/25', 6541635468451694865484654849),
    {'Checking Balance':100000, 'Saving Balance':2500}],
    [
    {'Name':'Brad K.'},
    {'Birthday':'02/07/85'},
    (7456, '11/25', 7987465464354684654684665178),
    {'Checking Balance':100000, 'Saving Balance':2500}]
  ] 

#-------------------- FOR TEST ONLY--------------------------------
'''
  adminInput = int(input("Please enter your choice:\n 1-Card info\n 2-user info\n"))
  if adminInput == 1:
    Data1 = int(input('Input1 (Cdt,exp,serial num):'))
    Data2 = int(input('Input1: (Cdt,exp,serial num):'))
    for info1 in users[Data1][Data2]:
      print(info1)
  elif adminInput == 2:
    Data3= int(input('Input3:'))
    Data4= int(input('Input4:'))
    Datatxt = input("Please enter the text search:")
    for info2 in users[Data3][Data4].get(Datatxt):
      print(info2)
'''
#---------------------------------------------------------------------

# ATM Info contains all ATM information like how much money stored in the ATM
def ATM_Info():
 # how much much are currently in the ATM safe
 # ATM Serial number
 # Cargorized bills
 # Conectivity check
  return


# Code trigger
DataSecurity()