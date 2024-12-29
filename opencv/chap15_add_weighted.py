"""배열병합"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "hsv.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)


# 배열병합
# 빨간색 영역을 검출하려 할 때, 빨간색 영역이 약 0 ~ 5와 약 170 ~ 179
# 두가지로 나눠져서 배열병합이 필요하다.
lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
upper_red = cv2.inRange(hsv, (170, 100, 100), (180, 255, 255))
added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)

red = cv2.bitwise_and(hsv, hsv, mask = added_red)
red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)

cv2.imshow("red", red)
cv2.waitKey()
cv2.destroyAllWindows()