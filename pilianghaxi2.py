# import av
import os
import shutil
import cv2
#from skimage.metrics import structural_similarity as compare_ssim
import time
from imutils import paths
# from imagehash import phash
# from PIL import Image as pil_image
# from imagehash import phash
import PIL
from PIL import Image
import imagehash



start = time.time()
#import cv2
import numpy as np


# def pHash(img):
#     img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img_sum = np.sum(img)
#     img_mean = img_sum / 64
#     img_finger = np.where(img > img_mean, 1, 0)
#     return img_finger


# # if __name__ == '__main__':
#     img1 = cv2.imread('11.png')
#     img1_phash = pHash(img1)
#
#     img2 = cv2.imread('12.jpg')
#     img2_phash = pHash(img2)
#
#     isquel = img1_phash == img2_phash
#     index = isquel == True
#     han = isquel[index]
#
#     # 两张图片的相似度
#     hanming = len(han)

if __name__ == '__main__':
    #pa = PyAvUtils('.\\pic1','.\\image1')
    #pa.do_video2image()
    dir = '.\\pic'
    img_path1 = '.\\image1'
    img_path2 = '.\\image'
    imgList = os.listdir(r"./" + dir)
    imgs_n = []
    imgList.sort(key=lambda x: int(x.split('.')[0]))
    print(imgList)
    for count ,filename in  enumerate (imgList):
        #filename = imgList[count]
        imgh = cv2.imread(dir + "/" + imgList[count])
        img = PIL.Image.open(dir + "/" + imgList[count])
        img_phash = imagehash.phash(img)
        #filename1 = imgList[count+1]
        img1 = PIL.Image.open(dir + "/" + imgList[count+1])
        img1_phash = imagehash.phash(img1)
        # isquel = img_phash == img1_phash
        # index = isquel == False
        # han = isquel[index]
        # hanming = len(han)
        # ssim = compare_ssim(img, img1, multichannel=True)
        #frame_dir = os.path.join(img_path1, '%d' % (count + 1))
        if img_phash-img1_phash>25:
            # imgs_n.append(imgList [count])
            cv2.imwrite(img_path2 + "/" + imgList[count], imgh)
            #print(imgList[count], imgList[count + 1], ssim)
        else:
            print('small_ssim',img_phash-img1_phash)
        count += 1

        if count >= len(imgList)-1:
             break
    # for currIndex ,image in enumerate (imgs_n):
    #     img3 = cv2.imread(dir + "/" + imgs_n[currIndex])
    #     # filename1 = imgList[count+1]
    #     img4 = cv2.imread(dir + "/" + imgs_n[currIndex + 1])
    #     ssim = compare_ssim(img3, img4, multichannel=True)
    #     if ssim < 0.5:
    #
    #         cv2.imwrite(img_path2 + "/" + imgs_n[currIndex], img3)
    #         #print(imgList[count], imgList[count + 1], ssim)
    #     #else:
    #         #print('small_ssim',imgList[count], imgList[count + 1], ssim)
    #     currIndex += 1
    #
    #     if currIndex >= len(imgs_n)-1:
    #          break
    end = time.time()
    print('Running time: %s Seconds' % (end - start))



