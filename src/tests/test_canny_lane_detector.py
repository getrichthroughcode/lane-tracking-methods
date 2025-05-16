# src/tests/test_canny_lane_detector.py

import os

import cv2
import numpy as np
import pytest

from src.utils.cannyLaneDetector import cannyLaneDetector


def test_readImg_success(tmp_path):
    """
    Test if readImg loads a valid image.
    """
    # Create a dummy image file (black square)
    test_img = np.zeros((50, 50, 3), dtype=np.uint8)
    img_path = tmp_path / "dummy.jpg"
    cv2.imwrite(str(img_path), test_img)

    detector = cannyLaneDetector(100, 50, 150)
    img = detector.readImg(str(img_path))

    assert isinstance(img, np.ndarray)
    assert img.shape == (50, 50, 3)


def test_readImg_fail():
    """
    Test if readImg handles invalid paths gracefully.
    """
    fake_path = "nonexistent_image.jpg"
    detector = cannyLaneDetector(100, 50, 150)
    img = detector.readImg(fake_path)

    assert img is None  # The method should return None on failure


def test_rgbToGray_success(tmp_path):
    """
    Test if rgbTogray converts proper image properly
    """
    # Create a dummy image files (black square)
    test_img1 = np.zeros((50, 50, 3), dtype=np.uint8)
    detector = cannyLaneDetector(100, 50, 150)
    img1 = detector.rgbToGray(test_img1)
    assert isinstance(img1, np.ndarray)
    assert img1.shape == (50, 50)


def test_rgbToGray_invalid_inputs(tmp_path, capsys):
    """
    Test if rgbToGray handles various invalid inputs gracefully.
    """
    test_cases = [
        (np.zeros((50, 50, 7), dtype=np.uint8), "OpenCV Error"),  # invalid channel size
        (
            np.zeros((50, 50), dtype=np.uint8),
            "OpenCV Error",
        ),  # already grayscale, but shape mismatch
        (None, "Unexpected Error"),  # None input
    ]

    detector = cannyLaneDetector(100, 50, 150)

    for img, expected_log in test_cases:
        result = detector.rgbToGray(img)
        captured = capsys.readouterr()
        assert result is None
        assert expected_log in captured.out


def test_applyGaussianBlur_success():
    img = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    detector = cannyLaneDetector(100, 50, 150)
    sigma = 2.5
    blurred = detector.applyGaussianBlur(img, sigma)
    assert not np.array_equal(img, blurred)
