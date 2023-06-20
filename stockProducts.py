products = {'tv':{"Name":"tv","Price":700, "Units":10 }, 'chair':{"Name":"chair","Price":40, "Units":5 }}
permission = ""

def searchProduct():
    found = False
    name = input("insert the product name's:\n")
    for p in products:
        if p == name: 
            found = True
            break
    if found == True :
        print(products[name])
    else:
        print("Into the stock there isn't a product with such name")

def addProduct():
    product = {}
    name = input("insert the product name's:\n")
    price = input("insert price product's:\n")
    units = input("insert units produt's:\n")
    product.update({"Name": name, "Price": price, "Units":units})
    products.update({name:product})

while(True):

    option = input("""Choose the option that you wish add a product:\n
                            1) Insert a product
                            2) Search a product                       
                       """)
    if(option == "1"):
        addProduct()
    elif(option == "2"):
        searchProduct()
    else:
        print("Insert charater available")
        break
