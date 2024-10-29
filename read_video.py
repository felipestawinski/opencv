import cv2 as cv

capture = cv.VideoCapture(0)
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

while True:
    changeRes(180, 180)
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break



changeRes(640, 480)

capture.release()
cv.destroyAllWindows()