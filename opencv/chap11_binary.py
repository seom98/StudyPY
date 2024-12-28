"""이진화"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 이진화
# 어느지점을 기준으로 값이 높거나 낮은 픽셀의 값을 대상으로 특정 연산을 수행할 때 사용한다.
# 일반적으로 검은색이나 흰색의 값으로 변경
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_TRUNC)

# 임계값 형식
# cv2.THRESH_BINARY	        dst = (src > thresh) ? maxval : 0
# (임곗값을 초과할 경우 maxval, 아닐 경우 0)

# cv2.THRESH_BINARY_INV	    dst = (src > thresh) ? 0 : maxval
# (임곗값을 초과할 경우 0, 아닐 경우 maxval)

# cv2.THRESH_TRUNC	        dst = (src > thresh) ? thresh : src
# (임곗값을 초과할 경우 thresh, 아닐 경우 변형 없음)

# cv2.THRESH_TOZERO	        dst = (src > thresh) ? src : 0
# (임곗값을 초과할 경우 변형 없음, 아닐 경우 0)

# cv2.THRESH_TOZERO_INV	    dst = (src > thresh) ? 0 : src
# (임곗값을 초과할 경우 0, 아닐 경우 변형 없음)

# cv2.THRESH_MASK	        검은색 이미지로 변경
# (마스크용)

# cv2.THRESH_OTSU	        오츠 알고리즘 적용
# (단일 채널 이미지에만 적용 가능)

# cv2.THRESH_TRIANGLE	    삼각형(Triangle) 알고리즘 적용
# (단일 채널 이미지에만 적용 가능)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
