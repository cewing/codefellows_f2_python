#!/usr/bin/python

def print_ (type_) :
    print
    if type_ == 'name' : 
        for key in donation_l.keys() : print key,
    print

def add_donor (donor_) :
    for i in donation_l.iterkeys() :
        if i == donor_ : break
    else :
        print u"Adding new donor to the Donation List"
        donation_l[donor_] = []            
    
def ask_for_amount () :
    amount = unicode(raw_input(u"Enter a donation amount : "))
    while not amount.isnumeric() :
        amount = unicode(raw_input(u"Enter a VALID donation amount : "))
    return amount

def add_new_amount(donor, amount) :
    donation_l.get(donor).append(amount)

def find_total_amount (donor) :
    total_ = 0
    for i in donation_l.get(donor) :
        total_ += float(i)
    return round(total_,2)
                
                
def send_mail () :
    donor_ = raw_input(u"Enter a Full Name :")
    if donor_ == 'list' :
        print_ ('name')
        return send_mail()
    
    add_donor(donor_)
    amount = ask_for_amount ()
    add_new_amount (donor_, amount)
    email_text = " "
    email_text = "\n\tDear %s,\n You've made total $%d donation. Thank you for your help.\n\tSincerely\n\n"%(donor_, find_total_amount(donor_))
    print email_text


def ave_amount (donor) :
    ave_  = 0
    count = 0
    for i in donation_l.get(donor) :
        count += 1
        ave_  += float(i)
    else :
        ave_ = ave_ / count
    return round(ave_,2)
    

def create_report () :
    new_list = []
    index = 0
    for i in donation_l.iterkeys() :
        new_list.append([find_total_amount(i), i, ave_amount(i)])
    
    new_list.sort()    
    print u" Donor Name      Total Donated   Ave. Donation  "
    print u"=============== =============== =============== "
    for i in new_list :
        print ' {:14s} {:14.2f} {:15.2f}'.format(i[1],i[0],i[2])
        




if __name__ == '__main__' :
    keys       = [u"David", u"Mark", u"Alice", u"Cindy", u"Martin" ]
    values = [ [50,150,150], [50,50,50], [80,100,100], [100,50,100], [200,150,150] ]
    donation_l = dict(zip(keys, values))
    
    time_to_exit = False
    
    while not time_to_exit :
        choice_ = raw_input (u"What do you want to do?\n1) Send a thank you mail\n2) Create a report\n3) Exit\n")
        if   choice_ == '1' : 
            send_mail ()
            print
        elif choice_ == '2' :
            create_report ()
            print
        elif choice_ == '3' :
            time_to_exit = True
        else :
            print u"Please enter a valid choice!"

    

    #write a program which prints the full path to all files in the current directory, one per line
    
    
    #write a program which copies a file from a source, to a destination (without using shutil, or the OS copy command)
    



