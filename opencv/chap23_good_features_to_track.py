"""코너검출"""
import os
import numpy as np
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "nemo.png")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)
dst = src.copy()
gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

# 코너검출 
# 윤곽선들의 코너를 검출
# 입력이미지, 코너최댓값, 코너품질, 최소거리, 마스크, 블록크기, 해리스코너검출기유무, 해리스코너개수
# 코너 최댓값 -> 검출할 최대 코너의 수를 제한합니다. 코너 최댓값보다 낮은 개수만 반환합니다.
# 코너 품질 -> 반환할 코너의 최소 품질을 설정합니다. 코너 품질은 0.0 ~ 1.0 사이의 값으로 할당할 수 있으며, 일반적으로 0.01 ~ 0.10 사이의 값을 사용합니다.
# 최소 거리 -> 검출된 코너들의 최소 근접 거리를 나타내며, 설정된 최소 거리 이상의 값만 검출합니다.
# 마스크 -> 입력 이미지와 같은 차원을 사용하며, 마스크 요솟값이 0인 곳은 코너로 계산하지 않습니다.
# 블록 크기 -> 코너를 계산할 때, 고려하는 코너 주변 영역의 크기를 의미합니다.
# 해리스 코너 검출기 유/무 -> 해리스 코너 검출 방법 사용 여부를 설정합니다.
# 해리스 코너 계수 -> 해리스 알고리즘을 사용할 때 할당하며 해리스 대각합의 감도 계수를 의미합니다.
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 5, blockSize=3, useHarrisDetector=True, k=0.03)
# 해당코드를 입력하여 사이클이 그려지도록 수정
corners = np.int32(corners)

for i in corners:
    cv2.circle(dst, tuple(i[0]), 3, (0, 0, 255), 2)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
