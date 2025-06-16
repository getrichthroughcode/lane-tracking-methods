import cv2 as cv
import sys
import os
tmp = sys.path[0]
sys.path[0] = tmp + "/../"
from utils.cannyLaneDetector import *

class cannyLaneTracker:
    def __init__(self, stream: str, detector: object, lowThresh : int, highThresh : int) -> None:
        self.detector = detector(25, lowThresh, highThresh)
        self.cap = cv.VideoCapture(stream)

    def _applyDetectorOnEachFrame(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            edges = self.detector.detectEdge(frame)
            lines = self.detector.applyHoughTransform(edges)
            result = frame.copy()
            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv.line(result, (x1,y1), (x2,y2), (0,0,255), 8)

            cv.imshow("Lane Detection", result)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv.destroyAllWindows()
        return None



tracker = cannyLaneTracker(stream = "data/raw/test_video.mp4", detector = cannyLaneDetector, lowThresh = 50, highThresh = 150)

tracker._applyDetectorOnEachFrame()






