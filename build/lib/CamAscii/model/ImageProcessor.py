import numpy as np
import cv2

class ImageProcessor:
    WIDTH_SCALE: int = 2

    @staticmethod
    def resize_image(image: np.ndarray, new_width: int = 100) -> np.ndarray:
        """Resize image

        Args:
            image (np.ndarray): Image to be resized
            new_width (int, optional): New width for the Image. Defaults to 100.

        Returns:
            np.ndarray: Image resized
        """
        original_height, original_width = image.shape
        aspect_ratio = original_width / original_height
        new_height = int(new_width / aspect_ratio / ImageProcessor.WIDTH_SCALE)
        resized_image = cv2.resize(image, (new_width, new_height))
        return resized_image
    
    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """To greyscale

        Args:
            image (np.ndarray): Image to convert in gray scale

        Returns:
            np.ndarray: Gray scale Image
        """
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)