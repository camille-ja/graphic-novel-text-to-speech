import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras import datasets, layers, models # type: ignore

#train model to recognize where text is (like coordinates of boxes)