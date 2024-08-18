import argparse

from .wrapper.VideoProcessor import VideoProcessor

def main():

    parser = argparse.ArgumentParser(description="RunTime Camera to ASCII Art")

    parser.add_argument(
        '-d', '--debug',
        action='store_true',
        help='Debug mode'
    )

    parser.add_argument(
        '-bw', '--black-white',
        action='store_true',
        help='Reverses the conversion scale'
    )

    args = parser.parse_args()

    video_processor = VideoProcessor(debug=args.debug)
    video_processor.process_video()

if __name__ == "__main__":
    main()
