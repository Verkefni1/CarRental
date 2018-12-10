

def search_customer(self, last_name = "", first_name = ""):
    if last_name + first_name == "":
        # UI needs to display that this is invalid, you need at least one parameter
    with open("../data/customer.csv", "r") as Customer_file:
        print("First_name - Last_name - Drivers_licence - Kennitala - Address - Customer_ID ")
        for line in Customer_file:
            line = line.lower().split(",")
            if last_name or if first_name in line:
                print(line)
# Get customer information
            elif:
                print("No results")


        