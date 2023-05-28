def get_total_price(books):
    return sum(i[2] for i in books)
        
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
        
    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
 

description = "this is a module named bookstore"


if __name__ == "__main__":
    book_list = [
        ("To Kill a Mockingbird", "Harper Lee", 2),
        ("The Great Gatsby", "F. Scott Fitzgerald", 5),
        ("Pride and Prejudice", "Jane Austen", 7),
        ("The Catcher in the Rye", "J.D. Salinger", 6),
        ("1984", "George Orwell", 15)
    ]
    
    total_price = get_total_price(book_list)
    print(total_price)