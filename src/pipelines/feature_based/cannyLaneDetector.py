"""
Author : Abdoulaye Diallo <abdoulayediallo338@gmail.com>
This file contains an implementation of a Lane detector 
based on the Canny process. 
"""

# === Import necessary libraries ===

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import os 

 

# === Canny class definition ===


class cannyLaneDetector:
    """
    This class contains methods and attributes for building
    a proper Canny edge/lane Detector. To help my
    understanding of the problem, I will implement a scratch
    version of a method then use a library which might contains
    an optimized version of what I wrote.
    """

    def __init__(
        self, gradThresh: float, firstThresh: float, secondThresh: float
    ) -> None:
        """
        Initialisation function.
        Params:
        -------
        imgPath (str):
            Image path
        gradThresh (float):
            a threshold for the gradient intensity
        firstThresh (float):
            lower threshold for the hysterisis thresholding
        secondThresh (float):
         upper threshold for the hysterisis thresholding

        Returns:
        ------
        None
        """
        self.gradThresh = gradThresh
        self.firstThresh = firstThresh
        self.secondThresh = secondThresh
 
    def detectEdge(self,img) -> np.ndarray:
        """
        apply the canny transformation to the given frame. 
        
        Parameters
        ----------
        imgPath : str 
            path of the image file
        """
        try:
                       
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            blurred = cv.GaussianBlur(gray,(5,5),2.4)

            edges = cv.Canny(blurred, self.firstThresh, self.secondThresh)

            return edges
        except FileNotFoundError as fnfError:
            print(f"[File Error]  {fnfError}")
        except ValueError as valError:
            print(f"[Value Error]  {valError}")
        except Exception as e:
            print(f"[Unexpected Error]  {e}")


    def applyHoughTransform(self, edges: np.ndarray) -> list:
        """
        Detect different lines in the frame.
        Parameters
        ----------
        edges : np.ndarray 
            Frame with detected edges apparent
        Returns 

        """
        try :
            if edges is None:
                raise ValueError("Input must be corrupted")
            lines = cv.HoughLinesP(edges,
                                   1,
                                   np.pi/180,
                                   threshold=100,
                                   minLineLength=5,
                                   maxLineGap= 70)
            return lines
        except Exception as e:
            print(f"[Unexpected error]  {e}")





