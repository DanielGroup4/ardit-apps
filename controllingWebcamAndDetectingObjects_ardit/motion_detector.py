from datetime import datetime
from distutils.command.build_scripts import first_line_re
import cv2, time
import pandas as pd

first_frame = None
status_list = [None, None]
times_list = []
df = pd.DataFrame(columns= ["Inicio", "Fin"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1] # umbral o limite
    thresh_frame = cv2.dilate(thresh_frame, None, iterations= 2)

    # deteccion contorno
    (conts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in conts:
        if cv2.contourArea(contour) < 1000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)

    status_list = status_list[-2:] # conseguir los ultimos dos estados del video

    if status_list[-1] == 1 and status_list[-2] == 0: # status_list = [0, 1]
        times_list.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1: # status_list = [1, 0]
        times_list.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1) # 1 milesima de segundo
    #print(gray)
    #print(delta_frame)

    if key == ord("p"):
        if status == 1:
            times_list.append(datetime.now())
        break


print(status_list)
print(times_list)

for i in range(0, len(times_list), 2):
    df = df.append({"Inicio": times_list[i], "Fin": times_list[i+1]}, ignore_index= True)

df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()

