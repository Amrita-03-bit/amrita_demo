class Book:

    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"title: {self.title}\n author : {self.author}\n price : {self.price}"

b=Book("Pyhton","alisha",8798)
print(b)
     
                