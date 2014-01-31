class Library(object):
    
    def __init__(self, name):
        self.shelves = []
        self.loc = {}
        self.name = name
        
    def shelf_count(self):
        print len(self.shelves)
        
    def library_books(self):
        print self.loc.keys()
        
        
class Shelf(object):  
    
    def __init__(self, name, library):
        self.name = name
        self.library = library
        self.contents = []
        library.shelves.append(self.name) 
        
    def content(self):
        shelf_books = [x for x in self.library.loc if self.library.loc[x] == self.name]
        print shelf_books
        print len(shelf_books)


class Book(object):
    
    def __init__(self, name):
        self.name = name
        
    def enshelf(self, nshelf):
        nshelf.contents.append(self.name)
        nshelf.library.loc[self.name] = nshelf.name
        
    def unshelf(self, ushelf):
        ushelf.contents.remove(self.name)
        del ushelf.library.loc[self.name]
        
        
publiclibrary = Library("Public")
nonfiction = Shelf("Nonfiction", publiclibrary)
fiction = Shelf("Fiction", publiclibrary)
zebra_facts = Book("Zebra Facts")
zebra_facts.enshelf(nonfiction)
unicorn_facts = Book("Unicorn Facts")
unicorn_facts.enshelf(fiction)
starstory = Book("Star Story")
starstory.enshelf(fiction)
publiclibrary.shelf_count()
publiclibrary.library_books()
fiction.content()
starstory.unshelf(fiction)
fiction.content()
publiclibrary.library_books()
