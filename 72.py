class product:

    def __init__(self,name,price):
        self.name=name
        self.price=price

    def discount(self):

        if self.price>1000:
            discount_num=self.price*10/100
            final_price = self.price-discount_num
            return final_price
        
        elif  self.price<1000:
            discount_num = self.price*5/100
            final_price = self.price - discount_num
            return final_price
        
p1=product("manisha",50000)
p2=product("payal",200) 

print(p1.discount())
print(p2.discount())
          


