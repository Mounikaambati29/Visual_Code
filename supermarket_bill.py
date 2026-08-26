name = input("Enter your Name:")

# List of items
lists = '''
Rice          Rs 20/kg
Dal           Rs 1/kg
jaggery       Rs 2/kg
Salt          Rs 5/kg
Paneer        Rs 10/kg
Horlicks      Rs 200/bottle
Onions        Rs 3/kg
Honey         Rs 2/liter
'''

# Declaration
price = 0
pricelist = []
totalprice = 0
Finalprice = 0
ilist = []
qlist = []
plist = []

# Rate for each item
items={'rice':20,'jaggery':2,'dal':1,'salt':5,'paneer':10,'Horlicks':200,'onions':3,'honey':2}

while True:
    option = input("Press 1 for list or 2 to exit: ")
    if option == '2':
        print("Thank you for shopping")
        break
    elif option == '1':
        print(lists)

        while True:
            inp1 = input("To buy press 1 or press 2 to exit: ")
            if inp1 == '2':
                print("Thank you for shopping")
                break
            elif inp1 == '1':
                item = input("Choose your items: ").lower()
                while True:
                    quantity_input = input("Enter quantity: ")
                    if quantity_input.isdigit():  # Check if input is a digit
                        quantity = int(quantity_input)
                        break
                    else:
                        print("Please enter a valid quantity.")
                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available. Sorry for the inconvenience.")
        if totalprice > 0:
            tax = (totalprice * 18) / 100
            finalamount = tax + totalprice
            print(25 * "=", "Pythonlife Supermarket", 25 * "=")
            print(28 * " ", "chennai")
            print("Name:", name, 30 * " ","August 04 2026")
            print(75 * "-")
            print("sno", 10 * " ", 'items', 8 * " ", 'quantity', 8 * " ", 'price')
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", 'Total amount:', 'Rs', totalprice)
            print("Tax amount", 25 * " ", 'Rs', tax)
            print(50 * "-")
            print(25 * " ", 'Final amount:', 'Rs', finalamount)
            print(50 * "-")
            print(10 * " ", "Thank you & Visit again")
            print(50 * "-")
