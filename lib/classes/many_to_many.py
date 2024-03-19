class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self): #get_name
        return self._name
    @name.setter
    def name(self, new_name): #set_name
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, "name"):
            self._name = new_name

        # code below was doing the thing but failing a test because it was raising an Exception. Avoided raising Exception with above code and flipping is/not isinstance logic to pass test. 
        
        # if not isinstance(new_name, str) or len(new_name) == 0:
        #     raise Exception("Name must be a string longer than zero characters.")
        # else:
        #     self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author is self])) #lmao

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self): 
    #thing to append is magazine.category. category lives nowhere else so idk how else you could access it.
    #maybe do list comp twice? once to aggregate all of the magazines the author has contributed to using article as the intermediary and one pulling from that list to create a smaller list

        first_list = [article.magazine for article in Article.all if article.author is self]
        if len(first_list) > 0:
            return list(set([magazine.category for magazine in first_list])) #biiiitch this worked
        else:
            return None


class Magazine:
    def __init__(self, name, category): 
        all = []
        self.name = name
        self.category = category

    @property #get_name
    def name(self):
        return self._name
    @name.setter #set_name
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    #see notes above regarding raising Exceptions/failing tests
    # def name(self, new_name):
    #     if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
    #         raise Exception("Magazine name must be a string between 2 and 16 characters")
    #     else:
    #         self._name = new_name

    @property
    def category(self): #get_category
        return self._category
    @category.setter #set_category
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category

    #at this point I'm keeping the additional versions of this code for posterity/practice
    # def category(self, new_category):
    #     if not isinstance(new_category, str) or len(new_category) == 0:
    #         raise Exception("Category must be a string longer than zero characters.")
    #     else:
    #         self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set([article.author for article in Article.all if article.magazine is self]))

    def article_titles(self):
        list_o_titles = [article.title for article in Article.all if article.magazine is self]
        if len(list_o_titles) > 0:
            return list_o_titles
        else:
            return None

    def contributing_authors(self): 
        all_contributors = [article.author for article in Article.all if article.magazine is self]
        #version of the code in contributors(). Can't call  contributors() because that returned list is by design unique and contributing_authors() will rely on there being duplicates. This is a list of all of the authors for all of the articles in that magazine as many times as they've written in that magazine. Need to return another list of  values if any given value appears in the above list at least twice.

        #count every element in the list comp above. If it appears twice or more, add it to a new list and return that list.

        for element in all_contributors:
            if all_contributors.count(element) >= 2:
                return [element for element in all_contributors]
            else: 
                return None


class Article: #article is intermediary 
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self): #get_title
        return self._title
    @title.setter #set_title
    def title(self, new_title):
        if isinstance(new_title, str) and (5 <= len(new_title) <= 50) and not hasattr(self, "title"):
            self._title = new_title
       
        # see notes above regarding raising Exceptions/failing tests

        # if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50) or hasattr(self, "title"):
        #     raise Exception("Article title must be a string between 5 and 50 characters and can't be reset one instantiated.")
        # else:
        #     self._title = new_title

    @property
    def author(self): #returns the author object for that article, so that article.author actually means something. get_author
        return self._author
    @author.setter #can be changed if new value is also an instance of Author object
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self): #get_magazine
        return self._magazine
    @magazine.setter #can be changed if new value is also an instance of the Magazine object
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine

