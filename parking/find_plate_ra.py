
import cv2
import imutils
import numpy as np
import pytesseract


cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
#pytesseract.pytesseract.tesseract_cmd=r"C:\Users\giorg\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
text2=[]
def find_pl_ra():
    joe = []
    for i in range(10):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grey scale
        gray = cv2.bilateralFilter(gray, 11, 17, 17)  # Blur to reduce noise
        edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
        cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            if len(approx) == 4:
                screenCnt = approx
                break
        if screenCnt is None:
            detected = 0
        else:
            detected = 1
        if detected == 1:
            cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

        try:

            mask = np.zeros(gray.shape, np.uint8)
            new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
            new_image = cv2.bitwise_and(img, img, mask=mask)
            (x, y) = np.where(mask == 255)
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]
            thr = cv2.threshold(src=Cropped, thresh=0, maxval=255, type=cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)[1]
            text = pytesseract.image_to_string(Cropped,config="--psm 6 -c tessedit_char_whitelist=0123456789KMTUYD")
            text2=text.split("\n")
            joe.append(text2[0])
            #cv2.imshow('Cropped', Cropped)
            k = cv2.waitKey(30) & 0xff
            if k == 27:  # press 'ESC' to quit
                break
        except Exception as e:
            print(e)
            joe.append("no")
        #cv2.imshow("dasd",img)
        #cv2.imshow("sasa", edged)
        #cv2.imshow("dsada", thr)
        k = cv2.waitKey(30) & 0xff
        if k == 27:  # press 'ESC' to quit
            break
    return joe


def self():
    pass
print(find_pl())



cv2.destroyAllWindows()
