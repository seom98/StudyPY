"""채널 분리와 병합"""
import os
import numpy as np
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "hsv.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)


# 채널 분리와 병합
# 이미지의 색상 공간의 채널을 분리하거나 합치기 위해 사용
# 예를 들어 BRG색상공간을 B,R,G로 분리
b, g, r = cv2.split(src)
inverse = cv2.merge((r, g, b)) # 순서를 변경하여 합치면 다른 색상으로 표현될 수 있음.

# 이미지[높이,너비,채널] 
# :, :, n을 입력할 경우, 이미지 높이와 너비를 그대로 반환하고 n번째 채널만 반환
b2 = src[:, :, 0]
g2 = src[:, :, 1]
r2 = src[:, :, 2]

# 빈공간 이미지.
height, width, channel = src.shape
zero = np.zeros((height, width, 1), dtype=np.uint8)
bgz = cv2.merge((b, r, zero))

cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)
cv2.imshow("inverse", bgz)
cv2.waitKey()
cv2.destroyAllWindows()
