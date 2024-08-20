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

    parser.add_argument(
        '-f', '--file',
        type=str,
        default=None,
        help='Select video to convert in ascii art'
    )

    parser.add_argument(
        '-v', '--virtual-cam',
        action='store_true',
        help='Run virtual cam of Ascii Art'
    )

    args = parser.parse_args()

    source = args.file if args.file != None else args.select_source
    video_processor = VideoProcessor(debug=args.debug, bw=args.black_white, source=source)

    if args.show_source:
        video_processor.show_camera_sources()
    elif args.virtual_cam:
        video_processor.run_virtual_camera()
    else:
        video_processor.process_video()

if __name__ == "__main__":
    main()
