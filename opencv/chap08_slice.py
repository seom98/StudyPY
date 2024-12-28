"""이미지 자르기"""
# 특정영역을 잘라내는 것을 관심영역이라고 한다.
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
src2 = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 자르기
# src[높이, 너비]로 관심영역설정
# .copy()를 이용하여 깊은 복사 진행 -> 안적으면 원본에도 영향을 미칠 수 있음(얕복)
dst = src[100:600, 200:700].copy()

# 아래 방법은 이미지에 특정 부분을 붙여넣는 방법
dst2 = src2.copy()
roi2 = src2[100:150, 120:170]
dst2[0:50, 0:50] = roi2

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("src2", src2)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
