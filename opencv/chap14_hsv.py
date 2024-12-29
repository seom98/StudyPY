"""색상, 채도, 명도"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "hsv.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# HSV공간은 색상을 표현하기에 간편한 색상 공간이다.
# 색상 -> 시각적 감각의 속성 0~179의 범위
# 채도 -> 이미지의 색상 깊이 0~255
# 명도 -> 색의 밝고 어두운 정도 0~255

# 색상 공간 변환 함수로 색상 공간을 BRG에서 HSV로 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# H 범위를 조정하여 특정 색상만 뽑아낼수 있다.
h = cv2.inRange(h, 8, 20) # 주황색은 8~20 범위를 가짐.
orange = cv2.bitwise_and(hsv, hsv, mask = h) # 마스크를 사용해 덧씌우기
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR) # 색상 공간을 HSV에서 BRG로 변환


cv2.imshow("h", h)
cv2.imshow("s", s)
cv2.imshow("v", v)
cv2.imshow("orange", orange)
cv2.waitKey()
cv2.destroyAllWindows()
