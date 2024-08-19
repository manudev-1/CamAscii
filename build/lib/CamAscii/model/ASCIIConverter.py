import numpy as np

class ASCIIConverter:
    def __init__(self, scale_type: str = 'WB') -> None:
        if scale_type == 'BW':
            self.SCALE: str = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """
        else:
            self.SCALE: str = """ '`^",:;Il!i~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwpqdbkhao*#MW&8%B@$"""
    
    def _pixels_to_ascii(self, image: np.ndarray) -> str:
        """Pixels to ASCII

        Args:
            image (np.ndarray): Array of pixel to be converted in ASCII

        Returns:
            str: ASCII
        """
        num_chars = len(self.SCALE)
        pixels = image.flatten()
        
        normalized_pixels = (pixels / 255.0) * (num_chars - 1)
        ascii_str = ''.join([self.SCALE[int(pixel)] for pixel in normalized_pixels])
        return ascii_str

    def image_to_ascii(self, image: np.ndarray) -> str:
        """Image to ASCII

        Args:
            image (np.ndarray): Image to be converted in ASCII

        Returns:
            str: ASCII
        """
        img_width = image.shape[1]
        ascii_str = self._pixels_to_ascii(image)
        ascii_str_len = len(ascii_str)
        ascii_img = ''
        for i in range(0, ascii_str_len, img_width):
            ascii_img += ascii_str[i:i+img_width] + '\n'
        return ascii_img