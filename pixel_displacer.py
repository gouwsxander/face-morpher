import warnings

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import map_coordinates

import warping

def _check_warps_intersect(warps: list[warping.Warp]) -> bool:
    """Checks if two ore more warps in a list of warps have intersecting areas of effect.

    Args:
        warps: List of warps to check.

    Returns:
        A boolean that is true only when there are intersecting warps.
    """
    for warp_1 in warps:
        for warp_2 in warps:
            if warp_1 != warp_2 and warp_1.bounding.intersects(warp_2.bounding):
                return True
            
    return False

def warp_image(image: np.ndarray, warp: warping.Warp) -> np.ndarray:
    """Applies a warp to an image.

    Args:
        image: Array of pixel values that is to be warpped.
        warp: The warp to be applied.

    Returns:
        The warpped image.
    """
    ...

def multi_warp_iamge(image: np.ndarray, warps: list[warping.Warp]) -> np.ndarray:
    """Applies multiple warps to an image. Provides a warning of those warps intersect.
    
    Args:
        image: Array of pixel values that is to be warpped.
        warps: A list of warps to be applied.

    Returns:
        The warpped image.
    """
    if _check_warps_intersect(warps):
        warnings.warn("Some warps are intersecting.")

    for warp in warps:
        image = warp_image(image, warp)


def _test():
    image = cv.imread("test_pictures/white_background.JPEG", cv.IMREAD_GRAYSCALE)

    height, width = image.shape

    x_coordinates, y_coordinates = np.meshgrid(np.arange(width, dtype=float), np.arange(height, dtype=float))
    x_coordinates, y_coordinates = x_coordinates.transpose(), y_coordinates.transpose()

    # # stretch out eyes
    # c = 469.5
    # w = 57
    # a = 1/2
    # y_coordinates -= a * (y_coordinates - c) * np.exp(- ((y_coordinates - c)/w)**2)

    # # squish mouth
    # c = 600
    # w = 45
    # a = -1/2
    # y_coordinates -= a * (y_coordinates - c) * np.exp(- ((y_coordinates - c)/w)**2)

    # # displace eyes
    # a = 40
    # c = 469.5
    # w = 90
    # x_coordinates += a * np.exp(-((x_coordinates - c)/w)**2)
    # x_coordinates += 10

    plt.imshow(map_coordinates(image, [y_coordinates, x_coordinates]), cmap="gray")
    plt.show()


