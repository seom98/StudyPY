"""캡쳐 및 녹화"""
import os
import datetime
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
gif_path = os.path.join(home_dir, "huh.gif")
capture = cv2.VideoCapture(gif_path)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
RECORD = False

# 27 = ESC, 26 = Ctrl + Z, 24 = Ctrl + X, 3 = Ctrl + C

while True:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open(gif_path)
    ret, frame = capture.read()
    # cv2.imwrite("경로 및 제목", 이미지)
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    if key == 27:
        break
    if key == 26:
        print("캡쳐")
        cv2.imwrite(home_dir + "/" + str(now) + ".png", frame)
    elif key == 24:
        print("녹화 시작")
        RECORD = True
        # cv2.VideoWriter("경로 및 제목", 비디오 포맷 코드, FPS, (녹화 파일 너비, 녹화 파일 높이))
        video = cv2.VideoWriter(home_dir + "/" + str(now) + ".mp4",
                                fourcc, 20.0, (frame.shape[1], frame.shape[0]))
    elif key == 3:
        print("녹화 중지")
        RECORD = False
        video.release() 
    if RECORD is True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()

# FourCC 종류
# CVID, Default, DIB, DIVX, H261, H263, H264, IV32, IV41, IV50, 
# IYUB, MJPG, MP42, MP43, MPG4, MSVC, PIM1, Prompt, XVID
