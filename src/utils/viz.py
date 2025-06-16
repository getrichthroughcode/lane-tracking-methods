import cv2 as cv
import numpy as np
from cannyLaneDetector import *
import json


def draw_lanes_on_binary_mask(label_entry: dict, image_size=(720, 1280)) -> np.ndarray:
    """
    Creates a binary image with ground-truth lanes drawn in white (255) on a black background.

    Args:
        label_entry (dict): A TuSimple label entry (one line from the JSON).
        image_size (tuple): Height x Width of the binary mask.

    Returns:
        np.ndarray: A binary mask (uint8) with white lane lines.
    """
    h, w = image_size
    mask = np.zeros((h, w), dtype=np.uint8)

    h_samples = label_entry["h_samples"]
    for lane in label_entry["lanes"]:
        points = [(x, y) for x, y in zip(lane, h_samples) if x != -2]
        for i in range(1, len(points)):
            cv.line(mask, points[i - 1], points[i], color=255, thickness=2)

    return mask



with open("data/raw/groundTruth.json", "r") as f:
    label_entry = json.loads(f.readline())

binary_mask = draw_lanes_on_binary_mask(label_entry)

cv.imshow("Binary Lane GT", binary_mask)
cv.waitKey(0)
cv.destroyAllWindows()

