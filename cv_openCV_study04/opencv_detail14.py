# power law transformation or gamma correction (감마보정)
# 이미지 개선중에 하나
# 출력 장비의 차이를 보정해주는 방법
# s = c * r의 gamma 제곱(**)
# s = 계산값
# r = 입력값
# c = scaling(증폭, 확장) 시킬 값
# gamma = 음수가 아닌 상수값


import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img = cv2.pyrDown(img)

for gamma in [0.1, 0.5, 1.5, 2.5]:
    img_gam = np.array(255*(img/255)**gamma, dtype="uint8")

    cv2.imshow("Oirginal", img)
    cv2.imshow("gamma Image"+ str(gamma), img_gam)

cv2.waitKey(0)
cv2.destroyAllWindows()