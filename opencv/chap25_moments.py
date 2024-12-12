"""모멘트"""
# 윤곽선(contour)이나 이미지(array)의 0차 모멘트부터 3차 모멘트까지 계산하는 알고리즘
# 공간 모멘트(spatial moments), 
# 중심 모멘트(central moments), 
# 정규화된 중심 모멘트(normalized central moments), 
# 질량 중심(mass center) 등을 계산
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "convex_hull.webp")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
dst = src.copy()

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

for i in contours:
    # cv2.moments(배열, 이진화 이미지)
    # 모멘트 함수로 면적, 평균, 분산 계산
    M = cv2.moments(i, False)
    cX = int(M['m10'] / M['m00'])
    cY = int(M['m01'] / M['m00'])
    
    # 중심점이 파란색 사이클
    cv2.circle(dst, (cX, cY), 3, (255, 0, 0), -1)
    cv2.drawContours(dst, [i], 0, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
