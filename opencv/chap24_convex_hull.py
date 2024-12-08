"""블록 껍질"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "convex_hull.webp")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours:
    # cv2.convexHull()를 활용해 윤곽선에서 블록 껍질을 검출
    # cv2.convexHull(윤곽선, 방향)
    # true -> 시계방향
    hull = cv2.convexHull(i, clockwise=True)
    cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)

# 블록껍질 검출은 스크랜스키(Sklansky) 알고리즘

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
