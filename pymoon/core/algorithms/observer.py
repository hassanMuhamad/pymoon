# !TODO:
#   - method that check if the folder contains files
#   - method that get information associated to a given file :: @param file
#   output: JSON based object
import os

class Observer():
    ''' # # # '''
    def __init__(self, Directory_instance):
        self.target = Directory_instance
        self.scene = Directory_instance.path
        self.list = Directory_instance.list_files()

    def hire(self):
        docs = ['pymoon_images', 'pymoon_texts', 'pymoon_videos']
        try:
            for doc_name in docs:
                self.target.create_subfolder(doc_name)
        except:
            print('The directories already exists')

    def cleanup(self):
        text_files = self.target.search_by_extension('.pdf')
        images_files = self.target.search_by_extension('.png')
        video_files = self.target.search_by_extension('.mp4')
        for files in text_files:
            print(files)
        for files in images_files:
            print(files)
        for files in video_files:
            print(files)


if __name__ == "__main__":
    pass
