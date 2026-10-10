
class Book:
    

    def __init__(self,title,author,):
        self.title = title
        self.author = author
        self.is_available = True


    def borrow(self):
        if not self.is_available:
            raise ValueError("Book is already borrowed")
        
        self.is_available = False

    def give_back(self):
        if self.is_available:
            raise ValueError("Book was not borrowed")
        
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    