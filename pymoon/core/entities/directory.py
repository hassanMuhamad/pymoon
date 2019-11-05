import os

class Directory():
    ''' # Directory class '''
    def __init__(self, path):
        ''' Class Constructor '''
        self.path = path

    def list_contents(self):
        ''' listing the sub-files and sub-directories '''
        return os.listdir(self.path)

    def list_files(self):
        ''' listing the sub-files '''
        listed_files = []
        for files in os.listdir(self.path):
            if os.path.isfile(files):
                listed_files.append(files)
        return listed_files

    def search_by_name(self, name, FLAG=0):
        ''' a seach method '''
        # @param :: name >> the name to search
        # @param :: FLAG >> decide the search target (either 0 for a file or 1 for a directory)
        # return Boolean
        if (FLAG == 0): # (FILE)
            for files in os.listdir(self.path):
                if os.path.isfile(files):
                    current_name, _ = os.path.splitext(files)
                    if current_name == name:
                        return True
        elif (FLAG == 1): # (FOLDER)
            for files in os.listdir(self.path):
                if os.path.isdir(files):
                    if files == name:
                        return True
        return False

    def search_by_extension(self, extension):
        ''' files searching method '''
        # @param :: extension >> files extension
        # returns >> a list for files with the given extension
        listed_files = []
        for files in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, files)):
                _, current_extension = os.path.splitext(files)
                if (current_extension == extension):
                    listed_files.append(files)
        return listed_files

    def create_subfolder(self, folder_name):
        ''' a method that create a sub-folder under directory path '''
        # @param :: folder name
        os.makedirs(self.path + '\\' + folder_name)

    def remove_file(self, file_name):
        ''' a method that remove an existing file '''
        os.remove(file_name)

    def rename_file(self, file_name, new_name):
        ''' a method that rename an existing file '''
        os.rename(file_name, new_name)

    # End of class

if __name__ == "__main__":
    pass
