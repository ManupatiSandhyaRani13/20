cart_items={}
while True:
    key=input("Enter the key ( or type exit to stop) : ")
    if key.lower()=='exit':
        break
    value=int(input(f"Enter the price for the key {key} : "))
    cart_items[key]=value
print(f"cart_items = {cart_items}")
Total_price=0
length=len(cart_items)
for i in cart_items:
    if cart_items[i]>25000:
        Total_price+=cart_items[i] #can also written as total=sum(dict.values())
print("Actual price : ",Total_price)
if Total_price>20000 or Total_price<=50000:
    discount=10
    discount_price=Total_price*(discount/100)
    final_price=Total_price-discount_price
    print(f"Total Price after 10% discount : {final_price}")
elif Total_price>50000:
    discount=15
    discount_price=Total_price*(discount/100)
    final_price=Total_price-discount_price
    print(f"Total Price  after 15% discount : {final_price}")
else:
    print(f"Total Price : {Total_price}")