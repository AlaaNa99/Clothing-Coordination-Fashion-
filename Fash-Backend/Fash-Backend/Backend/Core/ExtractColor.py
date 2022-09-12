import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# import glob
import skimage.io
import skimage.color
import skimage.filters


class extract_color:
    def __init__(self, image):
        self.image = skimage.io.imread(fname=image)
        #         sub_img = cv.cvtColor(self.image, cv.COLOR_RGB2HSV)
        self.lower_black = np.array([0, 0, 0])
        self.upper_black = np.array([180, 255, 30])

        self.lower_white = np.array([0, 0, 231])
        self.upper_white = np.array([180, 18, 255])

        self.lower_gray = np.array([0, 0, 40])
        self.upper_gray = np.array([180, 18, 230])

        self.lower_vinous = np.array([159, 50, 70])
        self.upper_vinous = np.array([175, 255, 255])

        self.lower_red = np.array([176, 50, 70])
        self.upper_red = np.array([180, 255, 255])

        self.lower_cyan = np.array([81, 50, 50])
        self.upper_cyan = np.array([103, 255, 255])

        self.lower_blue = np.array([104, 50, 50])
        self.upper_blue = np.array([111, 255, 255])

        self.lower_darkblue = np.array([112, 50, 50])
        self.upper_darkblue = np.array([128, 255, 255])

        self.lower_green = np.array([36, 50, 70])
        self.upper_green = np.array([80, 255, 255])

        self.lower_yellow = np.array([24, 50, 70])
        self.upper_yellow = np.array([26, 255, 255])

        self.lower_gold = np.array([20, 50, 70])
        self.upper_gold = np.array([23, 255, 255])

        self.lower_beg = np.array([13, 50, 70])
        self.upper_beg = np.array([19, 255, 255])

        self.lower_orange = np.array([10, 50, 70])
        self.upper_orange = np.array([12, 255, 255])

        #         lower_brown =np.array([0,0 ,96])
        #         upper_brown =  np.array([0, 255, 255])

        self.lower_oil = np.array([27, 50, 70])
        self.upper_oil = np.array([35, 255, 255])

        self.lower_purple = np.array([129, 50, 70])
        self.upper_purple = np.array([158, 255, 255])

    def most_frequent(self, List):
        #         return max(set(List), key = List.count)
        mx = max(set(List), key=List.count)
        return mx, List.index(mx)

    def center_image(self):
        hight, width, rise = self.image.shape
        mid_h = int(hight / 2)
        mid_w = int(width / 2)
        sub_img = self.image[mid_h - 35:mid_h + 35, mid_w - 25:mid_w + 25, :].copy()
        return sub_img

    def show_image(self):
        plt.imshow(self.image)
        plt.show()

    def show_center_image(self):
        plt.imshow(self.center_image())
        plt.show()

    def mask(self, lower, upper):
        imag_hsv = cv.cvtColor(self.center_image(), cv.COLOR_RGB2HSV)
        return cv.inRange(imag_hsv, lower, upper)

    def length(self, lower, upper):
        return len(self.mask(lower, upper)[self.mask(lower, upper) == 255])



    def check_range(self, value, lower, upper):
        return value >= lower and value <= upper



    def color(self):
        color_dic = {
            0: "black",
            1: "white",
            2: "gray",
            3: "red",
            4: "vinous",
            5: "cyan",
            6: "blue",
            7: "darkblue",
            8: "green",
            9: "yellow",
            10: "oil",
            11: "orange",
            12: "gold",
            13: "beg",
            14: "purple",
            15: "brown"
        }
        black_count = self.length(self.lower_black, self.upper_black)
        white_count = self.length(self.lower_white, self.upper_white)
        gray_count = self.length(self.lower_gray, self.upper_gray)
        red_count = self.length(self.lower_red, self.upper_red)
        vinous_count = self.length(self.lower_vinous, self.upper_vinous)
        cyan_count = self.length(self.lower_cyan, self.upper_cyan)
        blue_count = self.length(self.lower_blue, self.upper_blue)
        darkblue_count = self.length(self.lower_darkblue, self.upper_darkblue)
        green_count = self.length(self.lower_green, self.upper_green)
        yellow_count = self.length(self.lower_yellow, self.upper_yellow)
        oil_count = self.length(self.lower_oil, self.upper_oil)
        orange_count = self.length(self.lower_orange, self.upper_orange)
        #         brown_count = self.length(self.lower_brown, self.upper_brown)
        beg_count = self.length(self.lower_beg, self.upper_beg)
        gold_count = self.length(self.lower_gold, self.upper_gold)
        purple_count = self.length(self.lower_purple, self.upper_purple)

        list_count = np.array([black_count, white_count, gray_count, red_count, vinous_count, cyan_count,
                               blue_count, darkblue_count, green_count, yellow_count, oil_count, orange_count,
                               gold_count,
                               beg_count, purple_count])
        index = np.argmax(list_count)
        return color_dic[index]



