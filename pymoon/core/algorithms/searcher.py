import re, os

class Searcher():
    ''' Search methods '''
    def __init__(self, Directory_object, FLAG=0):
        self.target = Directory_object
        self.FLAG = FLAG

    def search_for(self, element):
        if (self.FLAG == 0): # Directory
            dirs = self.target.list_dirs()
            for dir in dirs:
                if (dir == element):
                    return True
        elif (self.FLAG == 1): # File
            files = self.target.list_files()
            for file in files:
                if (file == element):
                    return True
        return False

    def create_search_pattern(self, pattern):
        self.search_pattern = re.compile(pattern)

    def search_inside(self, element_name, isFile):
        if (isFile == True):
            file_path = os.path.join(self.target.path, element_name)
            file_content = open(file_path, mode='r')
            res = self.search_pattern.match(file_content)
            return res
        elif (isFile == False):
            try:
                sub_path = os.path.join(self.target.path, element_name)
                sub_list = os.listdir(sub_path)
                for element in sub_list:
                    if (element == element_name):
                        return True
            except:
                print('Error: Cannot access the directory')
        return False


if __name__ == "__main__":
    pass
