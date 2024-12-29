"""기하학적 변환"""
import os
import numpy as np
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "img.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)


# 기하학적 변환
# 이미지를 인위적으로 확대,축소,위치변경,회전,왜곡하는 것
# 아핀 변환과 원근 변환이 있다.
height, width, channel = src.shape

# 원근변환
# 네 점을 사용하여 픽셀을 재매핑한다.
# ->  매핑에 사용할 변환 전 원본 이미지의 픽셀 좌표(srcPoint)과 변환 후 결과 이미지의 픽셀 좌표(dstPoint)를 선언한다.
srcPoint = np.array([[400, 300], [600, 300], [700, 700], [300, 700]], dtype=np.float32)
dstPoint = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

# 원근 맵 행렬 생성 함수(cv2.GetPerspectiveTransform)
# 매핑 좌표에 대한 원근 맵 행렬을 생성할 수 있다.
matrix = cv2.getPerspectiveTransform(srcPoint, dstPoint)

# 원근 변환 함수
# 원근 맵 행렬에 대한 기하학적 변환을 수행할 수 있다.
# 입력이미지, 원근 맵 행렬, 출력이미지 크기
dst = cv2.warpPerspective(src, matrix, (width, height))

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
