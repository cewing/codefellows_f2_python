donations = dict([('Ame Rain', [1000, 2000, 2300]), ('Jon Lee', [1100, 2200, 500]), ('Yoko Ono', [10000, 2000]), ('Yuki Kobo',  [300]), ('Kimi Son', [700])])
choice = ''

while choice != 0:
    print ("   M A I N - M E N U")
    print ("1. Send a Thank You")
    print ("2. Create a Report")
    print ("0. Exit")
 
## Get input ###
    choice = raw_input('Enter your choice [0-2]: ')
 
### Convert string to int type ##
    choice = int(choice)
    #if choice == 0:
        #exit
    if choice == 1:
        name = raw_input("Please enter a name: ")
        if name == 'list':
            print donations.keys()
            name = raw_input("Please enter a name: ")
        if name not in donations.keys():
            donations.setdefault(name, [])
    #for i in range(len(donations)):
        if name in donations.keys():
            amount = raw_input("Enter donation amount: ")
            amount = int(amount)
            donations[name].append(amount)
            myfile = file("Thank you%s-%i.txt" % (name, amount),"w" )
            myfile.write('Dear %s, Thank you for your generous donation of $%i.\n' % (name, amount))
            myfile.close()
            print 'Dear %s, Thank you for your generous donation of $%i.' % (name, amount)
    elif choice == 2:
        for i in donations.keys():
            print '{:>1}'.format('%s') % i ,
            print '{:>15}'.format('%i') % sum(donations[i]), 
            print '{:>15}'.format('%i') % len(donations[i]),
            print '{:>15}'.format('%i') % (sum(donations[i])/len(donations[i]))
