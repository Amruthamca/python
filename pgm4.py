#Amrutha Biju
#21mca003
class Publisher:
    def read(self):
        print("Books")
class Book(Publisher):
    def title(self):
        print("Wings of fire")
    def author(self):
        print("APJ Abdul kalam")
class Python(Book):
    def price(self):
        print("200/-")
    def page(self):
        print("800")
p=Python()
p.read()
p.title()
p.author()
p.price()