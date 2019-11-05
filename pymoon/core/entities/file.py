# !TODO:
#   A class that takes either the file or the file name and extract relevant informations from it
#   implementation: >> algorithms/observer module
import os

class File():
    '''The abstruct representation of file'''
    def __init__(self, path=os.path.expanduser("~")):
        self.path = path
        self.name, self.extension = os.path.splitext(os.path.basename(path))
        # !TODO: check the status of the file and affect it to the associated field
        self.status = 0

    def get_file_path(self):
        return self.path

    def get_file_name(self):
        return self.name

    def get_file_extension(self):
        return self.extension

    def get_file_status(self):
        return self.status

    def change_file_name(self, new_file_name):
        try:
            os.rename(self.path, new_file_name)
            self.name = new_file_name
        except:
            print('Error: Cannot rename the file')

    def change_file_extension(self, new_file_extension):
        try:
            # !TODO: checks if the extension is accepteable according to the original one.
            pass
        except:
            print('Error: Cannot change the file extension')

    def move_file_to(self, new_path):
        try:
            # !TODO: checks if the file isNotVirtual
            pass
        except:
            print('Error: Cannot move the file')



def main():
    pass

if __name__ == "__main__":
    '''CONSOLE HANDLING'''
    file = File('C:/Users/21655/Desktop/week1_calendar.png')
    file_name = file.get_file_name()
    file_extension = file.get_file_extension()
    print(file.get_file_path())
    print(file_name, file_extension)
    print('--------------')
    file.change_file_name('calendar.png')
    file_name = file.get_file_name()
    file_extension = file.get_file_extension()
    print(file.get_file_path())
    print(file_name, file_extension)

