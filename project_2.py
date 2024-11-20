## project_2
# Library Management 

class Library:
    def __init__(self,name,bookslist):
        self.name=name
        self.bookslist=bookslist
        self.lendDict={}
    def displayBooks(self):
        print("We have following books in our library: ")
        for book in self.bookslist:
            print(book)
        
    def lendBook(self,book,user):
        if book in bookslist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("Book has been lended.Database updated")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print("Apologies!We don't have this book in our library")
    # def addBooks(self,book):
    #     if book in self.bookslist:
    #         print("Book already exists")
    #     else:
    #         self.bookslist.append(book)
    #         print("Book added")
    def addBooks(self,book):
        if book in bookslist:
            print("Book already exists")
        else:
            self.bookslist.append(book)
            bookDatabase=open(databaseName,"a")
            bookDatabase.write("\n")
            bookDatabase.write(book)
            print("Book added")
    
    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Book returned succesfully")
        else:

            print("Book doesn't exist in the book Lending Database")

def main():
    while(True):
        print(f"Welcome to the {library.name} library.Following are the options: ")
        choice="""
                    1.Display Books  
                    2.Lend a Book  
                    3.Add a Book  
                    4.Return a Book
                    """
        print(choice)
        userinput=input('Press Q to quit and C to continue: ')
        if userinput == 'C':
            userchoice=int(input('Select an option to continue: '))
            if userchoice == 1:
                library.displayBooks()
            elif userchoice == 2:
                book=input('Enter the name of the book you want to lend: ')
                user=input('Enter the name of the user: ')
                library.lendBook(book,user)
            elif userchoice == 3:
                book=input('Enter the name of book which you want to add to Database: ')
                library.addBooks(book)
            elif userchoice == 4:
                book=input('Enter the name of the book which you want to return: ')
                library.returnBook(book)
            else:
                print('Please choose a valid option: ')
        elif userinput == 'Q':
            break
        else:
            print('Please enter a valid option: ')


if __name__=='__main__':
    bookslist=[]
    databaseName=input('Enter the name of the datbase file with extension: ')
    bookDatabase=open(databaseName,'r')
    name=input("Name of the library")
    for book in bookDatabase:
        bookslist.append(book)
    library=Library(name,bookslist)
    main()
