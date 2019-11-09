import re, os

class Searcher():

    ''' A class contains to search methods '''

    def __init__(self, Directory_object, FLAG=0):
        ''' Searcher Class Constructor '''
        # Parameter:
        # (1) Directory_object: An instance of the Directory Class
        # (2) FLAG: either 1 (for files) or 0 (for directories)
        self.target = Directory_object
        self.FLAG = FLAG

    def search_for(self, element_name):
        ''' a method that search for element '''
        # Parameter:
        # (1) element_name: the name of the directory/file (based on the FLAG) to search
        # Return:
        # Boolean (True if found, False if not)
        if (self.FLAG == 1): # handling the directory case
            dirs = self.target.list_dirs()
            for dir in dirs:
                if (dir == element_name):
                    return True
        elif (self.FLAG == 0): # handling the file case
            files = self.target.list_files()
            for file in files:
                if (file == element_name):
                    return True
        return False

    def create_search_pattern(self, regular_expression):
        ''' a method that create a pattern to use in the search operation '''
        # Parameter:
        # (1) regular_expression: a regular expression express the pattern to follow
        self.search_pattern = re.compile(regular_expression)

    def search_based_on(self, pattern, element_name, isFile=True):
        ''' a method that search for a match based on a pattern object inside a file content '''
        # Parameter:
        # (1) pattern: a pattern to follow
        # (2) element_name: the element name
        # (3) isFile: flage (true if it is a file, False if not)
        # Return:
        # List contains the matches
        if (isFile == True):
            file_path = os.path.join(self.target.path, element_name)
            search_list = open(file_path, mode='r')
        elif (isFile == False):
            sub_path = os.path.join(self.target.path, element_name)
            search_list = os.listdir(sub_path)
        pattern_searcher = pattern.search(search_list)
        return pattern_searcher.group()

# End of class

if __name__ == "__main__":
    pass
