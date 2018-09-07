import numpy as np
import pytest
from responsive_wall.controller import transform_frame, WALL_SHAPE

@pytest.fixture
def frame():
    return np.random.rand(480, 640)

def test_transform_frame(frame):
    frame = transform_frame(frame)

    assert frame.shape == WALL_SHAPE
    assert frame.min() == 0.
    assert frame.max() == 1.
