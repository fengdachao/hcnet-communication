
import cv2
import numpy as np
from client import sendPic

#global imga

def pHash(img):
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_sum = np.sum(img)
    img_mean = img_sum / 64
    img_finger = np.where(img > img_mean, 1, 0)
    return img_finger
def comparehash(path1,path2):
    #print(imga)
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    img_phash=pHash(img1)
    img1_phash = pHash(img2)
    isquel = img_phash == img1_phash
    index = isquel == False
    han = isquel[index]
    hanming = len(han)
    print(hanming)
    if hanming>0:
        print ('hangming' ,hanming)
        sendPic(path2)    
            # imgs_n.append(imgList [count])
        # cv2.imwrite(img_path1 + "/" + imgList[count], img)
    # imga=img1
    #return img1





