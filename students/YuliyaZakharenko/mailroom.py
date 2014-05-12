donations = [['Ame Rain', [1000, 2000, 2300]], ['Jon Lee', [1100, 2200, 500]], ['Yoko Ono', [10000, 2000]], ['Yuki Kobo', [300]], ['Kimi Son', [700]]]
#print (30 * '-')
print ("   M A I N - M E N U")
#print (30 * '-')
print ("1. Send a Thank You")
print ("2. Create a Report")
#print (30 * '-')
 
## Get input ###
choice = raw_input('Enter your choice [1-2] : ')
 
### Convert string to int type ##
choice = int(choice)
 
if choice == 1:
    name = raw_input("Please enter a name: ")
    for i in range(len(donations)):
        if name in donations[i]:
            amount = raw_input("Enter donation amount: ")
            amount = int(amount)
            donations[i][1].append(amount)
            print donations

sum(donations[1][1])/len(donations[1][1])