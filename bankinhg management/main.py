import branchdb as br
import fddepositdb as fd
import cashierrrrdb as cash
import customerdb as cus


def main():
    while True:
        print('''\n ===== BANKING SYSTEM =====
        1. Branch Manager
        2. FD Manager
        3. Cashier
        4. Customer
        5. Exit''') 

        choice = int(input("Choose an option:- "))  

        if choice == 1:
            br.bm() 

        elif choice == 2:
            fd.fd() 

        elif choice == 3:
            cash.csh()  

        elif choice == 4:
            cus.cus() 

        elif choice==5:
            print("Thankyou for trusting our site!")    
            break 

        else:
            print("Invalid option ! Must choose an valid option ") 


main()    