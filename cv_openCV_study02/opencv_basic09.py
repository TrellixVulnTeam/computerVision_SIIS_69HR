import cv2
import numpy as np

img1 = np.zeros((352, 352,3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("./images/gray.jpg")
print(img2.shape)

# bitAnd = cv2.bitwise_and(img2, img1) # 1 and 1 만 1
# bitOr = cv2.bitwise_or(img2, img1)
# bitXor = cv2.bitwise_xor(img2, img1)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitNOT1", bitNot1)
cv2.imshow("bitNOT2", bitNot2)


cv2.waitKey(0)
cv2.destroyAllWindows()