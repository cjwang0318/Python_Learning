import cv2
import numpy as np
image = cv2.imread('./img_data/qrcode/test_sr2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 200)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    if len(approx) == 4:
        cv2.drawContours(image, [approx], 0, (0, 255, 0), 5)
scale_percent = 25  # percentage of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow('Rectangles Detected', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

