import cv2

video = cv2.VideoCapture(0)

if not video.isOpened():

    print("Cannot open camera")

    exit()

while True:

    ret, frame = video.read()

    if not ret:

        print("Frame cannot be recieved, please check your stream. Program exiting.")

        break

    frame = cv2.flip(frame, 1)

    hsv_color = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("frame", hsv_color)

    if cv2.waitKey(1) == ord("q"):

        break

video.release()

cv2.destroyAllWindows()
