import cv2
import os
from pygrabber.dshow_graph import FilterGraph
from pyvirtualcam import (PixelFormat, Camera)
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from ..model.ASCIIConverter import ASCIIConverter
from ..model.ImageProcessor import ImageProcessor

class VideoProcessor(cv2.VideoCapture):
    def __init__(self, source: int = 0, debug: bool = False, bw: bool = True) -> None:
        super().__init__(source)
        if not self.isOpened():
            raise ValueError("Errore nell'aprire la webcam.")
        self.ascii_converter = ASCIIConverter('BW' if bw else 'WB')
        self.image_processor = ImageProcessor()

        self.debug = debug

    def show_camera_sources(self):
        graph = FilterGraph()
        devices = graph.get_input_devices()
        for index, name in enumerate(devices):
            print(f"[{index}] : {name}" + " - Default" if index == 0 else "")

    def process_video(self) -> None:
        """
            Process Video
        """
        while True:
            ret, frame = self.read()

            if not ret:
                break


            gray_scale = self.image_processor.to_grayscale(frame)
            resized_frame = self.image_processor.resize_image(gray_scale)
            ascii_art = self.ascii_converter.image_to_ascii(resized_frame)

            if self.debug:
                cv2.imshow("Video", frame)
                cv2.imshow("Video BN", gray_scale)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.release()

    from PIL import Image, ImageDraw, ImageFont

    def run_virtual_camera(self):
        """
            Run virtual camera with monospaced font
        """
        width = 640
        height = 480
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
        max_line_length = 80

        try:
            font = ImageFont.truetype(font_path, 14) 
        except IOError:
            print("Font not found, using default.")
            font = ImageFont.load_default()

        with Camera(width=width, height=height, fps=20, fmt=PixelFormat.RGB) as cam:
            print(f'Using virtual camera: {cam.device}')
            while True:
                ret, frame = self.read()

                if not ret:
                    break

                gray_scale = self.image_processor.to_grayscale(frame)
                resized_frame = self.image_processor.resize_image(gray_scale)
                ascii_art = self.ascii_converter.image_to_ascii(resized_frame)

                ascii_lines = ascii_art.splitlines()
                ascii_lines = [line.ljust(max_line_length) for line in ascii_lines]

                image_pil = Image.new("RGB", (width, height), (0, 0, 0))
                draw = ImageDraw.Draw(image_pil)

                y0, dy = 10, 15
                for i, line in enumerate(ascii_lines):
                    y = y0 + i * dy
                    draw.text((10, y), line, font=font, fill=(255, 255, 255))

                image = np.array(image_pil)

                cam.send(image)
                cam.sleep_until_next_frame()

                if self.debug:
                    cv2.imshow("Video", frame)
                    cv2.imshow("ASCII Video", image)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        self.release()

    def release(self) -> None:
        """
            Stop video
        """
        self.release()
        cv2.destroyAllWindows()