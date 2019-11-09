import os

class Environment():

    ''' a bunch of working environement '''

    def __init__(self):
        ''' Environement Class Constructor'''
        self.OS_LANGUAGE = os.getenv('LANG') # OS language
        self.CURRENT_USER_HOME_DIR = os.path.expanduser("~")
        self.CURRENT_USER_DESKTOP = os.path.expanduser("~") + r'\Desktop'
        self.CURRENT_USER_DOCUMENT_DIR = os.path.expanduser("~") + r'\Documents'
        self.CURRENT_USER_DOWNLOADS_DIR = os.path.expanduser("~") + r'\Downloads'
        self.CURRENT_USER_IMAGES_DIR = os.path.expanduser("~") + r'\Pictures'
        self.CURRENT_USER_MUSIC_DIR = os.path.expanduser("~") + r'\Music'
        self.CURRENT_USER_VIDEOS_DIR = os.path.expanduser("~") + r'\Videos'

    def get_home_path(self):
        ''' GETTER METHOD '''
        return self.CURRENT_USER_HOME_DIR

    def get_documents_path(self):
        ''' GETTER METHOD '''
        return self.CURRENT_USER_DOCUMENT_DIR

    def get_images_path(self):
        ''' GETTER METHOD '''
        return self.CURRENT_USER_IMAGES_DIR

    def get_music_path(self):
        ''' GETTER METHOD '''
        return self.CURRENT_USER_MUSIC_DIR

    def get_videos_path(self):
        ''' GETTER METHOD '''
        return self.CURRENT_USER_VIDEOS_DIR

if __name__ == "__main__":
    wenv = Environment()
    print('WORKING ENV VARS:')
    print('CURRENT OS LANGUAGE |', wenv.OS_LANGUAGE)
    print('CURRENT USER HOME |', wenv.CURRENT_USER_HOME_DIR)
    print('CURRENT USER DESKTOP |', wenv.CURRENT_USER_DESKTOP)
    print('CURRENT USER DOCUMENTS |', wenv.CURRENT_USER_DOCUMENT_DIR)
    print('CURRENT USER IMAGES |', wenv.CURRENT_USER_IMAGES_DIR)
    print('CURRENT USER MUSIC |', wenv.CURRENT_USER_MUSIC_DIR)
    print('CURRENT USER VIDEOS |', wenv.CURRENT_USER_VIDEOS_DIR)