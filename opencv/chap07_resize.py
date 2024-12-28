"""이미지 크기조절"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "geunjagam.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 크기조절하기
# 입력이미지, 절대크기, 상대크기, 보간법
dst = cv2.resize(src, dsize=(640, 480), interpolation=cv2.INTER_AREA)
# 상대크기는 절대크기에 (0,0)를 할당한 후 사용
dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

# 보간법 종류
# cv2.INTER_NEAREST	        이웃 보간법
# cv2.INTER_LINEAR	        쌍 선형 보간법
# cv2.INTER_LINEAR_EXACT	비트 쌍 선형 보간법
# cv2.INTER_CUBIC	        바이큐빅 보간법
# cv2.INTER_AREA	        영역 보간법
# cv2.INTER_LANCZOS4	    Lanczos 보간법
# 기본적으로 쌍 선형 보간법을 가장 많이 사용한다.

# 확대 - 바이큐빅, 쌍선형
# 축소 - 영역 보간법

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
