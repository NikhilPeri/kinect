from skimage.measure import block_reduce
from skimage.transform import rescale

import freenect as kinect
import numpy as np
import logging
import sys

WALL_SHAPE=(4, 6)
FRAME_SHAPE=(480, 640)
DOWNSCALE=0.2
BLOCK_SIZE=(
    int(DOWNSCALE*FRAME_SHAPE[0]/WALL_SHAPE[0]),
    int(DOWNSCALE*FRAME_SHAPE[1]/WALL_SHAPE[1])
)

CALIBRATION_PATH='responsive_wall/tmp/calibration.frame'

def get_frame():
    try:
        frame, _ = kinect.sync_get_depth()
        frame = frame.astype(np.uint8)
        return frame
    except:
        logging.error('Failed to read frame')
        return np.full(FRAME_SHAPE, 255)

def transform_frame(frame):
    frame = rescale(frame, DOWNSCALE, anti_aliasing=False)
    frame = block_reduce(frame, BLOCK_SIZE, np.mean)
    frame = np.iinfo(np.uint8).max - frame

    return frame

def display_frame(frame):
    print frame

if __name__ == '__main__':
    calibration_frame = None
    with open(CALIBRATION_PATH) as calibration_file:
        calibration_frame = transform_frame(np.load(calibration_file))

    if calibration_frame is None:
        raise ValueError('Could not load calibration file: {}'.format(CALIBRATION_PATH))
        return
        
    # while True
    frame = get_frame()
    frame = transform_frame(frame)
    frame -= calibration_frame
    frame = np.where(frame < 0, frame, 0)
    display_frame(frame)
