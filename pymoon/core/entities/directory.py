import os, shutil

class Directory():

    ''' A representation of a folder as an Object associated to methods for its content handling '''

    def __init__(self, path):
        ''' Directory Class Constructor'''
        # Parameter:
        # (1) path: the associated system path
        self.path = path

    def list_contents(self):
        ''' listing sub-files and sub-directories '''
        # Return:
        # List contains name of all element under the associated path to the current object
        return os.listdir(self.path)

    def list_dirs(self):
        ''' listing sub-directories '''
        # Return:
        # List contains sub-directories names
        dir_content = self.list_contents()
        only_dirs = filter(os.path.isdir, dir_content)
        return only_dirs

    def list_files(self):
        ''' listing sub-files '''
        # Return:
        # List contains files names
        listed_files = []
        for files in os.listdir(self.path):
            if os.path.isfile(files):
                listed_files.append(files)
        return listed_files

    def search_by_name(self, name, FLAG=0):
        ''' a seach method '''
        # Parameters:
        # (1) name: the name of the directory/file to search
        # (2) FLAG: either 1 (for files) or 0 (for directories)
        # Return:
        # Boolean (True if found, False if not)
        if (FLAG == 0): # Handling the file case
            for files in os.listdir(self.path):
                if os.path.isfile(files):
                    current_name, _ = os.path.splitext(files)
                    if current_name == name:
                        return True
        elif (FLAG == 1): # handling the directory case
            for files in os.listdir(self.path):
                if os.path.isdir(files):
                    if files == name:
                        return True
        return False

    def search_by_extension(self, extension):
        ''' files searching method '''
        # Parameters:
        # (1) extension: the extension associated to files
        # Return:
        # List (contains the files names)
        listed_files = []
        for files in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, files)):
                _, current_extension = os.path.splitext(files)
                if (current_extension == extension):
                    listed_files.append(files)
        return listed_files

    def get_dir_size(self):
        ''' a method that return the directory size in bytes '''
        return os.path.getsize(self.path)

    def create_subfolder(self, folder_name):
        ''' a method that create a sub-folder under directory path '''
        # Parameters:
        # (1) folder_name: the name of the new folder
        os.makedirs(self.path + '\\' + folder_name)

    def remove_file(self, file_name):
        ''' a method that remove an existing file '''
        # Parameters:
        # (1) file_name: the name of the file to delete
        os.remove(file_name)

    def rename_file(self, old_name, new_name):
        ''' a method that rename an existing file '''
        # Parameters:
        # (1) old_name: the current name of file
        # (2) new_name: the new name of file
        os.rename(old_name, new_name)

    def move(self, element_name, destination_path, FLAG=0):
        ''' a method that move an element under the path field '''
        # Parameters:
        # (1) element_name: the name of the element to move
        # (2) FLAG: either 1 (for files) or 0 (for directories)
        # return:
        # Integer (0 in case of no error, 1 if an error has found)
        element_path = os.path.join(self.path, element_name)
        try:
            shutil.move(element_path, destination_path)
        except print(0):
            print('Error: Cannot move the element')

# End of class

def check_path(path):
    if (os.path.exists(path)):
        return True
    return False

def pathEndsWithAFile(path):
    if (os.path.isfile(path)):
        return True
    return False

def pathLeadsToDirectory(path):
    if (os.path.isdir(path)):
        return True
    return False

if __name__ == "__main__":
    pass
