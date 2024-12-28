"""확대 & 축소"""
# 이미지 피라미드를 활용하여 이미지를 확대하거나 축소할 수 있다.
# 가우시안 피라미드와 라플라시안 피라미드를 활용한다.
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "geunjagam.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 높이, 너비, 채널 지정
height, width, channel = src.shape

# 확대
dst = cv2.pyrUp(src, dstsize=(width * 2, height * 2), borderType=cv2.BORDER_DEFAULT)

# 축소
# borderType을 여러가지로 지정할 수 있다.
# cv2.BORDER_CONSTANT	    iiiiii | abcdefgh | iiiiiii
# cv2.BORDER_REPLICATE    	aaaaaa | abcdefgh | hhhhhhh
# cv2.BORDER_REFLECT	    fedcba | abcdefgh | hgfedcb
# cv2.BORDER_WRAP	        cdefgh | abcdefgh | abcdefg
# cv2.BORDER_REFLECT_101	gfedcb | abcdefgh | gfedcba
# cv2.BORDER_REFLECT101	    gfedcb | abcdefgh | gfedcba
# cv2.BORDER_DEFAULT	    gfedcb | abcdefgh | gfedcba
# cv2.BORDER_TRANSPARENT	uvwxyz | abcdefgh | ijklmno
# cv2.BORDER_ISOLATED	   관심 영역 (ROI) 밖은 고려하지 않음
dst2 = cv2.pyrDown(src)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()
