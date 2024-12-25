"""동영상,gif 화면에 띄우기"""
import os  # 파일 경로 조작을 위한 모듈
import cv2

# 사용자의 홈 디렉토리 경로 가져오기
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")

# gif 파일의 전체 경로 생성
# os.path.join()을 사용하여 운영 체제에 맞는 경로 구분자 사용
gif_path = os.path.join(home_dir, "huh.gif")
capture = cv2.VideoCapture(gif_path)

# 프레임을 지속적으로 받아오기
while cv2.waitKey(33) < 0:
    # 프레임이 마지막이라면 처음프레임으로 돌리기
    # 해당 코드가 없다면 한번 실행한 후 자동으로 윈도우가 닫아짐.
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read() # 프레임 읽기
    cv2.imshow("VideoFrame", frame) # 윈도우 창에 VideoFrame이라는 이름으로 프레임 띄우기

capture.release() # 메모리 해제 메서드로 카메라장치에서 받아온 메모리 해제
cv2.destroyAllWindows() # 모든 윈도우 닫기
