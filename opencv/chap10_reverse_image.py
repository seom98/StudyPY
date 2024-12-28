"""이미지 역상"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 색 반전 시키기
# 픽셀단위미다 비트연산을 적용 -> NOT 연산 - 각 자릿수의 값을 반대로 바꾸는 연산
# 입력이미지, 마스크로 출력이미지 생성
dst = cv2.bitwise_not(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
