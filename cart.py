class ShoppingCart(object):
	def __init__(self):
        self.item = []
        
    def add(self, item, price):
        for cart_item in self.items:
            if cart_item.item == item:
                cart_item.q += 1
                return 1
                
        self.items.append(Item(item, price))
        return self
    
    def item(self, index):
        return self.items[index-1].item
        
    def price(self, index):
        return self.items[index-1].price * self.items[index-1].q
    
    def total(self, sales_tax):
        sum_price = sum([item.price*item.q for item in self.items])
        return sum_price*(1.0 + sales_tax/100.0)
        
    def __len__(self):
        return sum([item.q for item in self.items])
        
class item(object):
    def __init__(self, item, price, q=1):
        self.item = item
        self.price = price
        self.q = q