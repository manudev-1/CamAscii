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

    parser.add_argument(
        '-ss', '--show-source',
        action='store_true',
        help='Shows available camera sources'
    )

    parser.add_argument(
        '-s', '--select-source',
        type=int,
        default=0,
        help='Selects the camera source by index'
    )

    args = parser.parse_args()

    video_processor = VideoProcessor(debug=args.debug, bw=args.black_white, source=args.select_source)

    if args.show_source:
        video_processor.show_camera_sources()
    else:
        video_processor.process_video()

if __name__ == "__main__":
    main()
