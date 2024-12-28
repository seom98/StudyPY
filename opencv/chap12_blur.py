"""흐림 효과"""
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 흐림효과
# 단순히 이미지를 흐리게 하는 것이 아닌, 노이즈를 제거해서 연산 시 계산을 빠르고 정확하게 수행하는데 도움을 줌
# 이미지의 해상도를 변경하는 경우에도 사용
# -> 이미지의 크기를 변경하면 존재하지 않는 데이터를 생성하거나 
#    존재하는 데이터를 줄여야 하므로 샘플링된 이미지를 재구성할 때 사용.

# 단순 흐림 효과 함수로 흐림효과 적용
# 입력이미지, 커널크기, 고정점, 테두리외삼법
# 커널크기로 흐림정도 설정
dst = cv2.blur(src, (10 , 10 ), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
