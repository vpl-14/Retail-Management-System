import json
user_details=dict()
items={
    "100": {
        "product_name": "Macbook Air",
        "price": 185000,
        "stock": 25,
        "rating": 4.9
    },
    "101": {
        "product_name": "iPhone 15",
        "price": 79900,
        "stock": 50,
        "rating": 4.8
    },
    "102": {
        "product_name": "Sony WH-1000XM5 Headphones",
        "price": 29990,
        "stock": 40,
        "rating": 4.7
    },
    "103": {
        "product_name": "Apple Watch Series 9",
        "price": 41900,
        "stock": 35,
        "rating": 4.6
    },
    "104": {
        "product_name": "iPad Pro 11-inch",
        "price": 81900,
        "stock": 20,
        "rating": 4.9
    },
    "105": {
        "product_name": "Sony PlayStation 5",
        "price": 54990,
        "stock": 15,
        "rating": 4.8
    },
    "106": {
        "product_name": "LG 27-inch 4K Monitor",
        "price": 26500,
        "stock": 30,
        "rating": 4.5
    },
    "107": {
        "product_name": "Canon EOS R50 Camera",
        "price": 68900,
        "stock": 10,
        "rating": 4.7
    },
    "108": {
        "product_name": "JBL Charge 5 Bluetooth Speaker",
        "price": 12999,
        "stock": 60,
        "rating": 4.6
    },
    "109": {
        "product_name": "Samsung T7 1TB Portable SSD",
        "price": 8500,
        "stock": 100,
        "rating": 4.8
    },
    "110": {
        "product_name": "Men's Classic White T-Shirt",
        "price": 499,
        "stock": 100,
        "rating": 4.5
    },
    "111": {
        "product_name": "Men's Denim Jacket",
        "price": 1999,
        "stock": 35,
        "rating": 4.7
    },
    "112": {
        "product_name": "Men's Formal Trousers",
        "price": 1299,
        "stock": 45,
        "rating": 4.3
    },
    "113": {
        "product_name": "Women's Floral Summer Dress",
        "price": 1499,
        "stock": 60,
        "rating": 4.8
    },
    "114": {
        "product_name": "Women's High-Waisted Jeans",
        "price": 1799,
        "stock": 80,
        "rating": 4.6
    },
    "115": {
        "product_name": "Women's Silk Saree",
        "price": 3500,
        "stock": 20,
        "rating": 4.9
    },
    "116": {
        "product_name": "Kids' Superhero Pajama Set",
        "price": 699,
        "stock": 120,
        "rating": 4.8
    },
    "117": {
        "product_name": "Kids' Winter Puffer Jacket",
        "price": 1299,
        "stock": 40,
        "rating": 4.7
    },
    "118": {
        "product_name": "Unisex Cotton Hoodie",
        "price": 1199,
        "stock": 75,
        "rating": 4.6
    },
    "119": {
        "product_name": "Unisex Running Sneakers",
        "price": 2499,
        "stock": 50,
        "rating": 4.5
    },
    "120": {
        "product_name": "Adjustable Doorway Pull-Up Bar",
        "price": 1499,
        "stock": 45,
        "rating": 4.6
    },
    "121": {
        "product_name": "Premium Non-Slip Yoga Mat",
        "price": 899,
        "stock": 100,
        "rating": 4.8
    },
    "122": {
        "product_name": "Heavy Duty Gymnastics Rings",
        "price": 2199,
        "stock": 30,
        "rating": 4.9
    },
    "123": {
        "product_name": "Resistance Band Set (5 Levels)",
        "price": 599,
        "stock": 150,
        "rating": 4.5
    },
    "124": {
        "product_name": "Steel Parallettes / Dip Bars",
        "price": 3499,
        "stock": 20,
        "rating": 4.7
    },
    "125": {
        "product_name": "10kg Adjustable Weighted Vest",
        "price": 2899,
        "stock": 15,
        "rating": 4.6
    },
    "126": {
        "product_name": "Liquid Chalk (250ml)",
        "price": 399,
        "stock": 80,
        "rating": 4.4
    },
    "127": {
        "product_name": "Whey Protein Isolate (1kg)",
        "price": 2799,
        "stock": 60,
        "rating": 4.8
    },
    "128": {
        "product_name": "Ab Roller Wheel with Knee Pad",
        "price": 449,
        "stock": 90,
        "rating": 4.3
    },
    "129": {
        "product_name": "Speed Jump Rope",
        "price": 299,
        "stock": 200,
        "rating": 4.5
    },
    "130": {
        "product_name": "Introduction to Algorithms (4th Edition)",
        "price": 1850,
        "stock": 40,
        "rating": 4.8
    },
    "131": {
        "product_name": "The C++ Programming Language",
        "price": 1250,
        "stock": 25,
        "rating": 4.7
    },
    "132": {
        "product_name": "Artificial Intelligence: A Modern Approach",
        "price": 1600,
        "stock": 30,
        "rating": 4.6
    },
    "133": {
        "product_name": "Data Science from Scratch",
        "price": 950,
        "stock": 55,
        "rating": 4.5
    },
    "134": {
        "product_name": "How to Win Friends and Influence People",
        "price": 299,
        "stock": 150,
        "rating": 4.8
    },
    "135": {
        "product_name": "Atomic Habits",
        "price": 499,
        "stock": 200,
        "rating": 4.9
    },
    "136": {
        "product_name": "Overcoming Gravity: Bodyweight Strength",
        "price": 3200,
        "stock": 15,
        "rating": 4.8
    },
    "137": {
        "product_name": "Project Hail Mary (Sci-Fi Thriller)",
        "price": 550,
        "stock": 80,
        "rating": 4.7
    },
    "138": {
        "product_name": "Dark Matter (Sci-Fi Novel)",
        "price": 450,
        "stock": 65,
        "rating": 4.6
    },
    "139": {
        "product_name": "Premium Leather Bound Notebook",
        "price": 350,
        "stock": 120,
        "rating": 4.4
    },
    "139": {
        "product_name": "Premium Leather Bound Notebook",
        "price": 350,
        "stock": 120,
        "rating": 4.4
    },
    "140": {
    "product_name": "Samsung Galaxy S24",
    "price": 74999,
    "stock": 45,
    "rating": 4.8
    },
    "141": {
        "product_name": "Google Pixel 8 Pro",
        "price": 106999,
        "stock": 25,
        "rating": 4.6
    },
    "142": {
        "product_name": "OnePlus 12",
        "price": 64999,
        "stock": 40,
        "rating": 4.7
    },
    "143": {
        "product_name": "iPhone 15 Pro",
        "price": 129900,
        "stock": 20,
        "rating": 4.9
    },
    "144": {
        "product_name": "Redmi Note 13 Pro+",
        "price": 31999,
        "stock": 80,
        "rating": 4.5
    },
    "145": {
        "product_name": "Nothing Phone (2)",
        "price": 37999,
        "stock": 35,
        "rating": 4.6
    },
    "146": {
        "product_name": "Motorola Edge 50 Pro",
        "price": 31999,
        "stock": 50,
        "rating": 4.4
    },
    "147": {
        "product_name": "Vivo V30 Pro",
        "price": 41999,
        "stock": 30,
        "rating": 4.5
    },
    "148": {
        "product_name": "Realme GT 6T",
        "price": 30999,
        "stock": 55,
        "rating": 4.6
    },
    "149": {
        "product_name": "iQOO 12",
        "price": 52999,
        "stock": 25,
        "rating": 4.7
    },
    "150": {
        "product_name": "Dyson V12 Vacuum Cleaner",
        "price": 49900,
        "stock": 18,
        "rating": 4.7
    },
    "151": {
        "product_name": "Philips Digital Air Fryer",
        "price": 9999,
        "stock": 45,
        "rating": 4.6
    },
    "152": {
        "product_name": "Instant Pot Duo 7-in-1",
        "price": 11990,
        "stock": 30,
        "rating": 4.8
    },
    "153": {
        "product_name": "Xiaomi Smart Air Purifier 4",
        "price": 14999,
        "stock": 40,
        "rating": 4.5
    },
    "154": {
        "product_name": "Nespresso Vertuo Coffee Machine",
        "price": 16500,
        "stock": 22,
        "rating": 4.4
    },
    "155": {
        "product_name": "Eufy RoboVac G30 Robot Vacuum",
        "price": 23999,
        "stock": 15,
        "rating": 4.3
    },
    "156": {
        "product_name": "Panasonic 27L Convection Microwave",
        "price": 15490,
        "stock": 25,
        "rating": 4.6
    },
    "157": {
        "product_name": "Kent Grand Plus Water Purifier",
        "price": 17450,
        "stock": 35,
        "rating": 4.5
    },
    "158": {
        "product_name": "Morphy Richards 4-Slice Toaster",
        "price": 4200,
        "stock": 55,
        "rating": 4.2
    },
    "159": {
        "product_name": "Havells Oro Digital Garment Steamer",
        "price": 6890,
        "stock": 28,
        "rating": 4.4
    },
    "160": {
        "product_name": "Maybelline Fit Me Matte Foundation",
        "price": 699,
        "stock": 120,
        "rating": 4.4
    },
    "161": {
        "product_name": "L'Oreal Paris Hyaluronic Acid Serum",
        "price": 999,
        "stock": 85,
        "rating": 4.6
    },
    "162": {
        "product_name": "Cetaphil Gentle Skin Cleanser",
        "price": 550,
        "stock": 150,
        "rating": 4.7
    },
    "163": {
        "product_name": "The Derma Co 10% Niacinamide Serum",
        "price": 599,
        "stock": 90,
        "rating": 4.5
    },
    "164": {
        "product_name": "Minimalist Sunscreen SPF 50",
        "price": 399,
        "stock": 200,
        "rating": 4.6
    },
    "165": {
        "product_name": "MAC Retro Matte Lipstick",
        "price": 1950,
        "stock": 45,
        "rating": 4.8
    },
    "166": {
        "product_name": "Biotique Bio Kelp Protein Shampoo",
        "price": 350,
        "stock": 110,
        "rating": 4.3
    },
    "167": {
        "product_name": "Plum Green Tea Pore Cleansing Face Wash",
        "price": 349,
        "stock": 130,
        "rating": 4.4
    },
    "168": {
        "product_name": "Mamaearth Onion Hair Oil",
        "price": 419,
        "stock": 95,
        "rating": 4.2
    },
    "169": {
        "product_name": "Neutrogena Hydro Boost Water Gel",
        "price": 1150,
        "stock": 70,
        "rating": 4.7
    },
    "170": {
        "product_name": "Ergonomic Office Chair",
        "price": 14999,
        "stock": 25,
        "rating": 4.6
    },
    "171": {
        "product_name": "Solid Wood Dining Table",
        "price": 34990,
        "stock": 12,
        "rating": 4.7
    },
    "172": {
        "product_name": "3-Seater Fabric Sofa",
        "price": 42500,
        "stock": 8,
        "rating": 4.5
    },
    "173": {
        "product_name": "King Size Bed with Storage",
        "price": 48999,
        "stock": 15,
        "rating": 4.8
    },
    "174": {
        "product_name": "Minimalist Study Desk",
        "price": 8499,
        "stock": 40,
        "rating": 4.4
    },
    "175": {
        "product_name": "4-Tier Wooden Bookshelf",
        "price": 6999,
        "stock": 30,
        "rating": 4.6
    },
    "176": {
        "product_name": "Modern Engineered Wood Wardrobe",
        "price": 24990,
        "stock": 10,
        "rating": 4.3
    },
    "177": {
        "product_name": "Marble Top Coffee Table",
        "price": 12499,
        "stock": 22,
        "rating": 4.5
    },
    "178": {
        "product_name": "Cushioned Bar Stools (Set of 2)",
        "price": 5999,
        "stock": 18,
        "rating": 4.2
    },
    "179": {
        "product_name": "Recliner Armchair",
        "price": 19999,
        "stock": 14,
        "rating": 4.7
    }
}

def ordering_system(multiplier):
    order_choice=int(input("Enter 1 to order any item, 2 to add items to cart and 3 to go back "))
    if(order_choice==3):
        categories()
    elif order_choice==1:
        product_key_input=input("Enter the product no. ")
        product_key=100+10*(multiplier-1)+int(product_key_input)-1
        tot_amt=items[str(product_key)]["price"]+(items[str(product_key)]["price"])*0.1
        print(f"The product details and amount to be paid are\n{items[str(product_key)]}\nTotal Price:{tot_amt}")
        proceed=int(input("Would u like to proceed with the payment?(1-Yes 0-No) "))
        if(proceed==1):
            if(user_details["wallet"]>=tot_amt):
                user_details["wallet"]-=tot_amt
                print("Transaction succesful!\n")
                user_details["past_order_count"]+=1
                user_details["past_orders"].append(f"{str(product_key)}")
                with open(f"{user_details["name"]}.json","w") as file:
                    json.dump(user_details,file)
                categories()
            else:
                print("Insufficient funds! Ordering failed")
                #call UIE function here
        else:
            categories()
    elif order_choice==2:
        product_key_input=input("Enter the product no. ")
        product_key=100+10*(multiplier-1)+int(product_key_input)-1
        user_details["added_to_cart"]["Orders_placed"].append(f"{str(product_key)}")
        user_details["added_to_cart"]["cart_count"]+=1
        print("Item added to cart :)")
        with open(f"{user_details["name"]}.json","w") as file:
            json.dump(user_details,file)
        categories()
    else:
        print("Wrong input. Repeat the process ")
        ordering_system(multiplier)

def electronics_category():
    print("\n--- Electronics ---")
    print("1. View Items\n2. Go Back")
    e_input=int(input("Enter your choice "))
    if(e_input==1):
        for i in range(100,110):
            print(f"\n\n{i-99}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Avaialble={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(1)
    elif(e_input==2):
        categories()
    else:
        print("Invalid input! Try again")
        electronics_category()
    
def clothing_category():
    print("\n--- Clothing ---")
    print("1. View Items\n2. Go Back")
    c_input=int(input("Enter your choice "))
    if(c_input==1):
        for i in range(110,120):
            print(f"\n\n{i-109}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Avaialble={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(2)
    elif(c_input==2):
        categories()
    else:
        print("Invalid input! Try again")
        clothing_category()

def fitness_category():
    print("\n--- Fitness and Training ---")
    print("1. View Items\n2. Go Back")
    f_input=int(input("Enter your choice "))
    if(f_input==1):
        for i in range(120,130):
            print(f"\n\n{i-119}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Avaialble={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(3)
    elif(f_input==2):
        categories()
    else:
        print("Invalid input! Try again")
        fitness_category()
    

def books_category():
    print("\n--- Books and Stationary ---")
    print("1. View Items\n2. Go Back")
    b_input=int(input("Enter your choice "))
    if(b_input==1):
        for i in range(130,140):
            print(f"\n\n{i-129}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Avaialble={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(4)
    elif(b_input==2):
        categories()
    else:
        print("Invalid input! Try again")
        books_category()

def mobile_category():
    print("\n--- Mobiles ---")
    print("1. View Items\n2. Go Back")
    m_input = int(input("Enter your choice: "))
    if m_input == 1:
        for i in range(140, 150):
            print(f"\n\n{i-139}. {items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Available={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(5)
    elif m_input == 2:
        categories()
    else:
        print("Invalid input! Try again")
        mobile_category()

def home_needs_category():
    print("\n--- Home Needs ---")
    print("1. View Items\n2. Go Back")
    h_input = int(input("Enter your choice "))
    if h_input == 1:
        for i in range(150, 160):
            print(f"\n\n{i-149}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Available={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(6)
    elif h_input == 2:
        categories()
    else:
        print("Invalid input! Try again")
        home_needs_category()

def beauty_category():
    print("\n--- Home Needs ---")
    print("1. View Items\n2. Go Back")
    K_input = int(input("Enter your choice "))
    if K_input == 1:
        for i in range(160, 170):
            print(f"\n\n{i-159}.{items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Available={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(7)
    elif K_input == 2:
        categories()
    else:
        print("Invalid input! Try again")
        beauty_category()
        
def furniture_category():
    print("\n--- Furniture ---")
    print("1. View Items\n2. Go Back")
    X_input = int(input("Enter your choice "))
    if X_input == 1:
        for i in range(170, 180):
            print(f"\n\n{i-169}. {items[str(i)]['product_name']}")
            print(f"Details: Price={items[str(i)]['price']}")
            print(f"         Quantity Available={items[str(i)]['stock']}")
            print(f"         Rating={items[str(i)]['rating']}\n\n")
        print("\n")
        ordering_system(8)
    elif X_input == 2:
        categories()
    else:
        print("Invalid input! Try again")
        furniture_category()


def categories():
    print("\n" + "="*35)
    print("             CATEGORIES            ")
    print("="*35)
    print("1. Electronics")
    print("2. Clothing")
    print("3. Fitness and Training")
    print("4. Books and Stationary")
    print("5. Mobiles")
    print("6. Home and Everyday Needs")
    print("7. Beauty")
    print("8. Furniture and Appliances")
    print("9. Log Out")
    print("-" * 35)
    
    cat_choice = input("Enter your choice (1-9): ")
    
    if cat_choice == '1':
        electronics_category()
    elif cat_choice == '2':
        clothing_category()
    elif cat_choice == '3':
        fitness_category()
    elif cat_choice == '4':
        books_category()
    elif cat_choice == '5':
        mobile_category()
    elif cat_choice == '6':
        home_needs_category()
    elif cat_choice == '7':
        beauty_category()
    elif cat_choice == '8':
        furniture_category()
    elif cat_choice == '9':
        print("Returning to main menu...")
        UIE()
    else:
        print("Invalid choice, please select a number between 1 and 9.")
        categories() 

def account_details():
    with open(f"{user_details["name"]}.json","r") as file:
        data = json.load(file)
        print(f"Name: {data["name"]}")
        print(f"Phone no.: {data["phno"]}")
        print(f"Address: {data["add"]}")
        print(f"Email: {data["email"]}")
    UIE()

def Cart():
    with open(f"{user_details["name"]}.json","r") as file:
        data = json.load(file)
        if data["added_to_cart"]["cart_count"]==0:
            print("N0 items added to cart")
        else:
            print("Items:\n")
            for i in data["added_to_cart"]["Orders_placed"]:
                print(items[i])
        if data["past_order_count"]==0:
            print("N0 items were ordered")
        else:
            print("Orders:\n")
            for i in data["past_orders"]:
                print(items[i])
    UIE()

def Wallet():
    with open(f"{user_details["name"]}.json","r") as file:
        data = json.load(file)
        print("Bank Account no.",data["bank_ac_no"])
        print("Amount in Wallet: ",data["wallet"])
        UIE()

def UIE():
    print("*******User Interface********")
    print("1.Account details\n2.Cart\n3.Categories\n4.Wallet\n5.Log Out\n")
    input3 = int(input("Enter number:"))
    if input3==1:
        account_details()
    elif input3==2:
        Cart()
    elif input3==3:
        categories()
    elif input3==4:
        Wallet()
    elif input3==5:
        print("Thank you for using our Retail system!")
    else:
        print("Invalid Number")
        UIE()

def user_login():
    global user_details
    print("1.Log in\n2.Create account\n")
    login_input2=int(input("Enter your choice "))
    if(login_input2==2):
        name=user_details["name"]=input("Enter your name ")
        user_details["phno"]=int(input("Enter your phone number "))
        user_details["add"]=input("Enter your address ")
        user_details["email"]=input("Enter your email ")
        user_details["password"]=input("Set a strong password for your account ")
        user_details["bank_ac_no"]=input(("Enter your bank account number "))
        user_details["wallet"]=int(input("Enter amount of money you want to transfer to your wallet"))
        user_details["past_orders"]=list()
        user_details["past_order_count"]=0
        user_details["added_to_cart"]=dict()
        user_details["added_to_cart"]["cart_count"]=0
        user_details["added_to_cart"]["Orders_placed"]=list()
        with open(f"{name}.json","w") as file:
            json.dump(user_details,file)
        UIE()
    elif(login_input2==1):
        name=input("Enter Username ")
        try:
            with open(f"{name}.json","r") as file:
                data=json.load(file)
                for i in range(4,0,-1):
                    password=input("Enter your account password ")
                    if(password==data["password"]):
                        print("Welcome")
                        user_details.update(data)
                        UIE()
                        break
                    else:
                        if i-1==0 :
                            print("Sorry malicious actions detected - banning account for 24 hours ")
                            return
                        print(f"Wrong password {i-1} more tries left")
        except FileNotFoundError:
            print("Did you enter your user name correctly?")
            user_login()
    else:
        print("Wrong input, Try again ")
        user_login()

user_login()

