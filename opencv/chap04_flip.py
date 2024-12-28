"""이미지 대칭시키기"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
dst = cv2.flip(src, 0)
# =0 -> 상하대칭
# <0 -> 상하좌우대칭
# >0 -> 좌우대칭

cv2.imshow("src", src)
# cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
