import sys, os, cv2

class Detect():

    ''' Detection class based on images '''

    def __init__(self, image_path):
        ''' Constructor class '''
        self.image_path = image_path

    def set_classifier(self, classifier_name):
        ''' a method that sets the classifier used in further processing '''
        # Parameters:
        # (1) classifier_name: the name of the classifier
        if (classifier_name == "haar"):
            data = os.path.join(os.getcwd(), r'data\\haarcascade_frontalface_default.xml')
            self.classifier= cv2.CascadeClassifier(data)

    def image_reader(self):
        ''' read the image using the given path '''
        self.image = cv2.imread(self.image_path)
        self.grayscale = cv2.cvtcolor(self.image, cv2.COLOR_BGR2GRAY)


    def detect_haar(self, scaleFactor=1.1, minNeighbors=5, minSize=(1,1), flags=cv2.CASCADE_SCALE_IMAGE):
        ''' implement the HAAR Cascade to the image '''
        self.faces = self.classifier.detectMultiScale(
            self.grayscale,
            scaleFactor,
            minNeighbors,
            minSize,
            flags
        )

    def show_result(self, color=(255, 0, 0)):
        ''' draws rectangle arround the detected faces and show result image '''
        # Parameters:
        # (1) color: the rectangle border-color
        for(x, y, w, h) in self.faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), color, 2)
        cv2.imshow("detected",self.image)
        cv2.waitkey(0)

# End of class
