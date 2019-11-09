import sys, cv2, os

class Detect():
    def __init__(self, image_path):
        self.image_path = image_path

    def set_classifier(self, classifier_name):
        if (classifier_name == "haar"):
            data = os.path.join(os.getcwd(), r'data\\haarcascade_frontalface_default.xml')
            self.classifier= cv2.CascadeClassifier(data)

    def img_reader(self): 
        self.image = cv2.imread(self.image_path)
        self.grayscale = cv2.cvtcolor(self.image, cv2.COLOR_BGR2GRAY)
    

    def detect_haar(self, scaleFactor = 1.1, minNeighbors = 5, minSize = (1,1)):
        self.faces = self.classifier.detectMultiScale(
            self.grayscale,
            scaleFactor,
            minNeighbors,
            minSize,
            flags = cv2.CASCADE_SCALE_IMAGE
        )

    def draw_rec(self):
        for(x, y, w, h) in self.faces:
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255,0,0), 2)    
        cv2.imshow("detected",self.image)
        cv2.waitkey(0)    
