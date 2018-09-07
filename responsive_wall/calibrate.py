import os
import numpy as np
from responsive_wall.controller import get_frame, CALIBRATION_PATH


if __name__ == '__main__':
    raw_input('Press [Enter] when ready for calibration .. ')
    frame = get_frame()
    if os.path.exists(CALIBRATION_PATH):
        os.remove(CALIBRATION_PATH)

    with open(CALIBRATION_PATH, 'w+') as calibration_file:
        np.save(calibration_file, frame)
