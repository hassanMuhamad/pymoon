# !TODO:
#   A class that takes either the file or the file name and extract relevant informations from it
#   implementation: >> algorithms/observer module
import os, shutil

class File():

    '''The abstruct representation of file'''

    def __init__(self, path=os.path.expanduser("~")):
        ''' File Class Constructor'''
        # Parameter:
        # (1) path: the associated path to the file
        self.path = path
        self.name, self.extension = os.path.splitext(os.path.basename(path))


    def get_file_path(self):
        ''' GETTER METHOD '''
        return self.path

    def get_file_name(self):
        ''' GETTER METHOD '''
        return self.name

    def get_file_extension(self):
        ''' GETTER METHOD '''
        return self.extension

    def change_file_name(self, new_file_name):
        ''' Changes the file name '''
        # Parameter:
        # (1) new_file_name
        try:
            os.rename(self.path, new_file_name)
            self.name = new_file_name
        except:
            print('Error: Cannot rename the file')

    def change_file_extension(self, new_file_extension):
        # !TODO:
        pass

    def move_file_to(self, new_path):
        ''' Moves the file to a new location '''
        # Parameter:
        # (1) new_path: the new location
        try:
            shutil.move(self.path, new_path)
            pass
        except:
            print('Error: Cannot move the file')

# End of class

if __name__ == "__main__":
    pass

