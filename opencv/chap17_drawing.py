"""도형그리기"""
import numpy as np
import cv2

# 우선 빈 검정화면 그리기 
src = np.zeros((768, 1366, 3), dtype=np.uint8)

# 직선그리기
# 입력이미지, 시작좌표, 도착좌표, 색상, 두께, 선형타입, 비트시프트
src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)

# 원그리기
# 입력이미지, 중심점, 반지름, 생상, 두께, 선형타입, 비트시프트
src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)

# 사각형 그리기
# 입력이미지, 좌측상단모서리좌표, 우측하단모서리좌표, 색상, 두께, 선형타입, 비트시프트
src = cv2.rectangle(src, (500, 200), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)

# 호 그리기
# dst = cv2.ellipse(src, center, axes, angle, startAngle, endAngle, color, thickness, lineType, shift)
# 입력이미지, 중심점, 장축과 단축, 각도, 시작각도, 도착각도, 색상, 두께, 선형타입, 비트시프트
src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 180, (255, 255, 0), 2)

# numpy형태의 위치좌표
pts1 = np.array([[100, 500], [300, 500], [200, 600]])
pts2 = np.array([[600, 500], [800, 500], [700, 600]])

# poly함수를 사용하여 위치좌표로 다각형을 그릴 수 있다.
# 내부가 비워진 다각형
# 입력이미지, 선들의 묶음, 처음과 끝좌표의 연결여부, 색상, 두께, 선형타입, 비트시프트
src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)

# 내부가 채워진 다각형
# 입력이미지, 선들의 묶음, 색상, 두께, 선형타입, 비트시프트, 오프셋
# 오프셋은 좌표를 (x,y)만큼 움직여서 이동시킬 수 있다.
src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)

# 문자그리기
# 입력이미지, 문자열, 좌측상단모서리좌표, 글꼴, 글자크기, 색상, 두께, 선형타입, 기준좌표
# 기준좌표는 불린값 -> 좌측하단모서리좌표로 기준을 잡을 경우 true
src = cv2.putText(src, "SEO_M98", (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 3)

cv2.imshow("src", src)
cv2.waitKey()
cv2.destroyAllWindows()


# 선형 타입 종류
# cv2.FILLED	내부 채우기
# cv2.LINE_4	4점 이웃 연결
# cv2.LINE_8	8점 이웃 연결
# cv2.LINE_AA	AntiAlias

# 글꼴 종류
# cv2.FONT_HERSHEY_SIMPLEX	        보통 크기의 산세리프 글꼴	        -
# cv2.FONT_HERSHEY_PLAIN	        작은 크기의 산세리프 글꼴	        -
# cv2.FONT_HERSHEY_DUPLEX	        보통 크기의 산세리프 글꼴	        정교함
# cv2.FONT_HERSHEY_COMPLEX	        보통 크기의 세리프 글꼴	            -
# cv2.FONT_HERSHEY_TRIPLEX	        보통 크기의 세리프 글꼴	            정교함
# cv2.FONT_HERSHEY_COMPLEX_SMALL	작은 크기의 손글씨 글꼴	            -
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX	보통 크기의 손글씨 글꼴	            -           
# cv2.FONT_HERSHEY_SCRIPT_COMPLEX	보통 크기의 손글씨 글꼴	            정교함
# cv2.FONT_ITALIC	                기울임 꼴	                        -