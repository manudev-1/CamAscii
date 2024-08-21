# CamAscii

**CamAscii** is a Python application that captures video from your webcam and converts it into real-time ASCII art. This project demonstrates how to use OpenCV for video capture and ASCII conversion, including options for debugging and customization.



## Authors

- [@manudev-1](https://github.com/manudev-1)


## Features

- Real-time video capture from webcam
- Conversion of video frames to ASCII art
- Optional debug mode for displaying grayscale video (flag -d)
- Shows Camera available on your PC (flag -ss)
- You can select a camera (flag -s DEFAULT: 0)
- Convert video file to ASCII Art (flag -f)
- Chose ASCII shadow scale (flag: -bw DEFAULT: WB)
- Output to a Virtual Cam (Required OBS)


## Installation

### Prerequisites

Please make sure you have installed Python 3.6 or later on your system. You will also need `pip` to install the required packages.

### Clone the Repository

```bash
git clone https://github.com/yourusername/CamAscii.git
cd CamAscii
pip install .
camascii --help
```
