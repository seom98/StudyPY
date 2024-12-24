"""카메라 출력"""
import cv2

capture = cv2.VideoCapture(0) # 카메라 선택하기 - 여기에서는 0번카메라를 선택하는 것
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 카메라 가로 세팅
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 카메라 세로 세팅

# 프레임을 지속적으로 받아오기
while cv2.waitKey(33) < 0: # 어떤 키라도 입력되기 전까지 33ms마다 반복문을 실행
    ret, frame = capture.read() # 프레임읽기
    cv2.imshow("VideoFrame", frame) # 윈도우 창에 VideoFrame이라는 이름으로 프레임 띄우기

capture.release() # 메모리 해제 메서드로 카메라장치에서 받아온 메모리 해제
cv2.destroyAllWindows() # 모든 윈도우 닫기
cv2.destroyWindow("VideoFrame") # 특정윈도우 닫기
