
# Creating Product class 
class Product:
    def __init__(self,product_name, product_price, category):
        self.product_name=product_name
        self.product_price=product_price
        self.category= category

    def update_price(self, percent_change, is_increased):
        if is_increased is True:
            self.product_price = self.product_price+(self.product_price*percent_change)
        else:
            self.product_price = self.product_price-(self.product_price*percent_change)
            
        return self.product_price
        
        
    def print_info(self):
        print("product name:", self.product_name, "product price:", self.product_price, "product category:", self.category)

# Creating instances of the product class
computer = Product(product_name ="Lenovo", product_price=2000, category="tech")
mobile = Product(product_name="Xiaomi", product_price=1000, category="tech")
headphone = Product(product_name="skullcandy", product_price=500, category="tech")

computer.print_info()
mobile.print_info()
headphone.print_info

print(computer.update_price(percent_change=.01, is_increased=True))
print(mobile.update_price(percent_change=.01, is_increased=False))


#creating Store class

class Store:
    def __init__(self,store_name):
        self.store_name= store_name
        self.products= []

    def add_product(self, products):
        self.products.append(products)
        
        
    def sell_product(self,products):
        self.products.remove(products)

    
    
    def print_store_products(self):
        for i in range (0, len(self.products)):
            print(self.products[i].product_name)

    


#Creating instances of store class

walmart = Store(store_name="Walmart")

walmart.add_product(computer)


walmart.add_product(mobile)


walmart.add_product(headphone)


walmart.print_store_products()

walmart.sell_product(mobile)

walmart.print_store_products()










# walmart.products.append(computer)
# print(walmart.products[0].product_name)

# print(walmart.products[0].print_info())









        
        






        