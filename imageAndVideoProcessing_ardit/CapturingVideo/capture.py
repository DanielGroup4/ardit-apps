from tabnanny import check
import cv2, time

video = cv2.VideoCapture(0)

a = 0
while True:
    a += 1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1) # 1 milesima de segundo

    if key == ord("p"):
        break

print(a) # frames per second
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

