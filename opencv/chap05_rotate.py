"""이미지 회전시키기"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "geunjagam.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 높이, 너비, 채널 지정
# 높이와 너비를 이용하여 회전 중심점을 설정한다.
height, width, channel = src.shape

# 2*3 회전 행렬 생성 함수로 회전 변환 행렬을 계산한다.
 # 중심점, 각도, 비율로 매핑 변환 행렬 생성
matrix = cv2.getRotationMatrix2D((width/2,height/2), 90, 1)

# 아핀 변환 함수로 회전 변환을 계산
# 원본이미지, 아핀맵행렬, 출력이미지크기
dst = cv2.warpAffine(src, matrix, (width,height))


cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
