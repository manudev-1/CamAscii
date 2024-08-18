import cv2
import os

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

    def release(self) -> None:
        """
            Stop video
        """
        self.release()
        cv2.destroyAllWindows()