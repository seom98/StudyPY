"""이미지 화면에 띄우기"""
import os  # 파일 경로 조작을 위한 모듈
import cv2

# 사용자의 홈 디렉토리 경로 가져오기
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")

# 이미지 파일의 전체 경로 생성
# os.path.join()을 사용하여 운영 체제에 맞는 경로 구분자 사용
image_path = os.path.join(home_dir, "lunar.jpg")

# 이미지 파일 읽기
# cv2.IMREAD_ANYCOLOR 플래그는 이미지를 원본 형식 그대로 읽음
# (컬러 이미지는 컬러로, 그레이스케일 이미지는 그레이스케일로)
image = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 읽은 이미지를 화면에 표시
# "Moon"은 생성될 창의 이름
cv2.imshow("Moon", image)

# 키 입력을 기다림
# 0을 인자로 주면 무한정 기다림 (아무 키나 누르면 다음으로 진행)
cv2.waitKey()

# 생성된 모든 OpenCV 창 닫기
cv2.destroyAllWindows()
