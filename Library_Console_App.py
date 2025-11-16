#Name       -       Vishesh Kumar
#Date       -       Nov.16,2025
#Project    -       Library Inventory & Borrowing System
#Course     -       BCA (Cyber Security)
#Subject    -       Problem Solving with Python

#Task-1 Welcome

print("="*30)
print("Welcome To The Library")
print("Inventory & Borrow System")
print("="*30)
print("Manage books,Search title,Borrow and Return books")
print("="*30)
books={}
borrowed={}
while True:
    print("Library Menu")
    print("1-Add Book")
    print("2-View Books")
    print("3-Search Book")
    print("4-Borrow Book")
    print("5-Return Book")
    print("6-Exit")
    choice = input("Enter Your Choice: ")    
#Task-2 Adding Books to List Part=

    if choice=="1":
        print("Adding New Book")
        book_id=input("Enter Book ID-")
        if book_id in books:
            print("Book ID Already Exists...")
            continue
        title=input("Enter Book Title-")
        author=input("Enter Book Authors Name-")
        try:
            copies = int(input("Enter No. of Copies to be Added-"))
        except ValueError:
            print("Invalid No. Book not Added")
            continue
        books[book_id]={"title":title,"author":author,"copies":copies}
        print("Book is Added")
#Task-3 Book List Part=

    elif choice=="2":
        print("Library Book List")
        if not books:
            print("No Books Avilable at the Current Moment to be Issued")
        else:
            print(f"{'ID':<10}{'TITLE':<25}{'AUTHOR':<20}{'COPIES'}")
            for book_id, info in books.items():
                print(f"{book_id:<10}{info['title']:<25}{info['author']:<20}{info['copies']}")
            print()
#task3 Search Part =

    elif choice=="3":
        print("Book Search")
        print("1-Search by Book ID")
        print("2-Search by Book Title")
        search_choice = input("Enter Choice-")
        if search_choice=="1":
            book_id=input("Enter Book ID-")
            if book_id in books:
                info = books[book_id]
                print(f"Found: {info['title']} by {info['author']} ({info['copies']} copies)")
            else:
                print("Not Found")
        elif search_choice=="2":
            title=input("Enter Book Title-").lower()
            found=False
            for info in books.values():
                if title in info['title'].lower():
                    print(f"{info['title']} by {info['author']} - Copies: {info['copies']}")
                    found = True
            if not found:
                print("Book Not Found.")
        print()
#Task-4 Borrow Book Part=

    elif choice=="4":
        print("Book Borrowing")
        student=input("Enter Students Name-")
        if student in borrowed:
            print("This Student has already borrowed a book, no new books will be issued")
            continue
        book_id=input("Enter Book ID to Borrow-") 
        if book_id in books:
            if books[book_id]["copies"]>0:
                books[book_id]["copies"] -= 1
                borrowed[student]=book_id
                print("Book Issued")
            else:
                print("Not Available")
        else:
            print("Invalid Book ID")
#Task-5 Return Part=

    elif choice=="5":
        print("Returning Books")
        student = input("Enter Students Name-")
        if student in borrowed:
            book_id=borrowed[student]
            books[book_id]["copies"]+=1
            del borrowed[student]
            print("Book Return Accepted")
            borrowed_list=[f"{s}->{b}"for s,b in borrowed.items()]
            print("Currently Borrowed Books-", borrowed_list,)
        else:
            print("No books issued by this student this student")
#Task-6 Exitting Loop=

    elif choice=="6":
        print("Exiting the app...tata waves*")
        break
    else:
        print("invalid choice")
