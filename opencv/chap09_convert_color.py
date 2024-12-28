"""색상공간변환"""
# 색상공간변환은 본래의 색상 공간에서 다른 색상 곤간으로 변환할 때 사용한다.
import os
import cv2
home_dir = os.path.expanduser("~/Documents/StudyPY/StudyPY/Image")
image_path = os.path.join(home_dir, "kuromi.jpg")

src = cv2.imread(image_path, cv2.IMREAD_ANYCOLOR)

# 색상공간변환
# 입력이미지, 색상 변환 코드, 출력 채널 으로 출력이미지 생성
# 색상변환코드 -> 원본 이미지 색상 공간2결과 이미지 색상 공간
# 출력채널 -> 기본값을 사용하여 자동으로 채널수 결정
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 채널범위
# CV_8U	    0 ~ 255
# CV_16U	0 ~ 65535
# CV_32F	0 ~ 1

# 색상공간코드
# BGR   	    Blue, Green, Red 채널	                -
# BGRA	        Blue, Green, Red, Alpha 채널	        -
# RGB	        Red, Green, Blue 채널	                -
# RGBA	        Red, Green, Blue, Alpha 채널	        -
# GRAY	        단일 채널	                            그레이스케일
# BGR565	    Blue, Green, Red 채널	                16 비트 이미지
# XYZ	        X, Y, Z 채널	                        CIE 1931 색 공간
# YCrCb	        Y, Cr, Cb 채널	                        YCC (크로마)
# HSV	        Hue, Saturation, Value 채널	            색상, 채도, 명도
# Lab	        L, a, b 채널	                        반사율, 색도1, 색도2
# Luv       	L, u, v 채널	                        CIE Luv
# HLS	        Hue, Lightness, Saturation 채널	        색상, 밝기, 채도
# YUV	        Y, U, V 채널	                        밝기, 색상1, 색상2
# BG, GB, RG	디모자이킹	                            단일 색상 공간으로 변경
# _EA	        디모자이킹	                            가장자리 인식
# _VNG	        디모자이킹	                            그라데이션 사용


cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()
