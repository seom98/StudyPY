"""가장자리 검출"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "geunjagam.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 가장자리 검출
# 이미지 상에서 가장자리는 전경과 배경이 구분되는 지점. 밝기가 큰폭으로 변하는 지점을 가장자리로 판단
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 입력이미지에서 가장자리 검출

# 소벨 함수
# dst = cv2.Sobel(src, ddepth, dx, dy, ksize, scale, delta, borderType)은 
# 입력 이미지(src), 출력 이미지 정밀도, dx, dy, 커널 크기, 비율, 오프셋, 테두리 외삽법 으로 
# 결과 이미지(dst)를 반환한다.
sobel = cv2.Sobel(gray, cv2.CV_8U, 0, 1, 3)
# dx + dy >= 1 이어야함. 0의 값은 해당 방향으로 미분하지 않음을 의미

# 라플라시안 함수
# 밝은부분에서 발생한 것인지 어두운부분에서 발생한 것인지 알 수 있음.
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

# 캐니 함수
# 강한 가장자리를 검출하는데에 목적을 둔 알고리즘
# 생성형 AI에서도 중요하게 쓰임.
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()
