import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD
from .models import UserModel, HomeModel, FirstScreenModel,SecondScreenModel,ThirdScreenModel
from .serializer import HomeSerializer, SecondScreenSerializer, ThirdScreenSerializer
from Backend.settings import MEDIA_ROOT, MEDIA_URL
from keras.datasets import fashion_mnist
from keras.models import load_model
# from keras.utils import load_img
from keras.models import Sequential
from keras.utils import to_categorical
from keras.utils import img_to_array
from keras.utils import load_img
import cv2
from PIL import Image


class modelCNN:
    def thershold(self,img):
        src = cv2.imread(img, 0)
        maxValue = 255
        thresh = 0
        blur = cv2.GaussianBlur(src, (5, 5), 0)
        retval, dst = cv2.threshold(blur, thresh, maxValue, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        print("fffffffffffffffrrrrrrrrrrrrrrrrrr   ", retval)
        return retval

    def open(self,img):
        col = Image.open(img)
        gray = col.convert('L')
        # bw = gray.point(lambda x: 0 if x==255 else 255, '1')
        bw = gray.point(lambda x: 0 if x > self.thershold(img) else 255, '1')
        str = "C:/Users/bayan/OneDrive/Desktop/girl/cyan222.jpg"
        bw.save(str)
        return str

    def load_image(self,filename):
        # load the image
        img = load_img(filename, grayscale=True, target_size=(28, 28))
        # convert to array
        img = img_to_array(img)
        # reshape into a single sample with 1 channel
        img = img.reshape(1, 28, 28, 1)
        # prepare pixel data
        img = img.astype('float32')
        img = img / 255.0
        return img

    def run_example(self,str):
        img = self.load_image(str)
        model = load_model('C:/Users/bayan/OneDrive/Desktop/final_model.h5')
        predict_x = model.predict(img)
        classes_x = np.argmax(predict_x, axis=1)
        print("jjjjjjjjjjjjjjjjjjjjjjjjjjj")
        print("gggggggggggggggggggggggggggggg  ", classes_x[0])
        return classes_x[0]

    def nameclothes(self ,classes_x):
        if classes_x == 0:
            print("T_Shirt")
            return "T_Shirt"
        elif classes_x == 1:
            print("Trouser")
            return "Trousers"
        elif classes_x == 2:
            print("Shirt")
            return "Shirt"
        elif classes_x == 3:
            print("dress")
            return "dress"
        elif classes_x == 4:
            print("Jacket")
            return "Jacket"
        # elif classes_x == 5:
        #     return ""
        elif classes_x == 6:
            print("Shirt")
            return "Shirt"
        # elif classes_x == 7:
        #     return ""
        # elif classes_x == 8:
        #     return ""
        # elif classes_x == 9:
        #     return ""


