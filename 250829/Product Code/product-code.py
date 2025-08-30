product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Product:
    def __init__(self,n,c):
        self.n = n
        self.c = c

p1 = Product("codetree",50)
p2 = Product(product_name, product_code)

print("product", p1.c, "is", p1.n)
print("product", p2.c, "is", p2.n)