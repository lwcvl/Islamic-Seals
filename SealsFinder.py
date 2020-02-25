import cv2
import numpy as np


threshold = 80
debugThresh = False


font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 1
fontColor              = (0,0,0)
lineType               = 3


template1 = cv2.imread("seal1.jpg", cv2.IMREAD_GRAYSCALE)
name1 = "Sultanic"
name2 = "Hanif"

widthTemplate1, heigthTemplate1 = template1.shape[::-1]
print("Going to work!")


def matchingTemplate(image, seal, name, accuracy, color, w,h):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # The magic function. Notice how 'loc' can be tweaked with a different accuracy
    result = cv2.matchTemplate(gray_img, seal, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= accuracy)


    FindAll = False
    # This code only runs to see all results. Move along for attempt to narrow it down to the one location.
    if FindAll:
        for pt in zip(*loc[::-1]):
            cv2.rectangle(gray_img, pt, (pt[0] + w, pt[1] + h), color, 3)
        small = cv2.resize(gray_img, (0, 0), fx=0.3, fy=0.3)

        cv2.imshow("grey", small)
        cv2.moveWindow("grey", 0, 0)
        print("Check your image to see all!")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit()

    ret,thresh1 = cv2.threshold(gray_img,threshold,255,cv2.THRESH_BINARY)

    # For debugging only: to see how the threshold holdsup (value can be changed)
    if debugThresh:
        small = cv2.resize(thresh1, (0, 0), fx=0.3, fy=0.3)
        cv2.imshow("Threshold at {0}".format(threshold), small)
        cv2.moveWindow("Threshold at {0}".format(threshold), 0, 0)
        print("Check your image to see threshold!")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        exit()

    checkForUniques = True

    xCoordinates = []
    yCoordinates = []

    for pt in zip(*loc[::-1]):
        print("Still working...")
        regionOfInterest = thresh1[pt[1]:pt[1] + h, pt[0]:pt[0] + w]

        if checkForUniques == True:
            unique_elements, counts_elements = np.unique(regionOfInterest, return_counts=True)

            if (len(unique_elements) == 2 and unique_elements[0] == 0 and counts_elements[0] > 800):
                xCoordinates.append(pt[0])
                yCoordinates.append(pt[1])
                # cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 3)
        else:
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), color, 3)

    if xCoordinates:
        medianX = int(np.median(xCoordinates))
        medianY = int(np.median(yCoordinates))
    else:
        if accuracy < 0.32:
            print("Seal not found")
            return()
        else:
            print("Didn't find anything at accuracy {0}, searching again.".format(accuracy))
            matchingTemplate(image,seal,name, accuracy-0.02, color,w,h)

    certainty = "With certainty " + str(round(accuracy,2))
    xCloseToMedian = []
    for x in xCoordinates:
        if x > medianX-30:
            xCloseToMedian.append(x)
    if xCloseToMedian:
        cv2.rectangle(img, (medianX, medianY), (medianX + w, medianY + h), color, 3)
        cv2.rectangle(img, (medianX, medianY+h), (medianX + w, medianY + h+20), color, -1)
        cv2.putText(img, certainty, (medianX, medianY + h + 20),font,fontScale,fontColor, lineType)
        cv2.imwrite("seal1."+image, img)

with open('stabiPages.txt', 'r') as f:
    pages = f.read().split('\n')


for page in pages:
    matchingTemplate(page, template1,name1, 0.45, (255, 255, 0),widthTemplate1, heigthTemplate1)