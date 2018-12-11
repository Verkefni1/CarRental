

def search_customer(self, last_name = "", first_name = ""):
    if last_name + first_name == "":
        return False
        #UI needs to display that this is invalid, you need at least one parameter
    with open("../data/customer.csv", "r") as Customer_file:
        #print("First Name - Last Name - Drivers Licence - Kennitala - Address - Customer_ID ")
        for line in Customer_file:
            line = line.lower()
            if last_name in line or if first_name in line:
                print(line)
#Get customer information
            elif:
                #print("No results")
                return 0


        