import sys
import os
import os.path as ops

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

from handdet import HandDet
from utils import Camera


# 手识别的测试
hdet = HandDet(ops.join(root, "handdet/output/best_model"))
acq_camera = Camera(updata_func=hdet.infer)
print("Start acquisition, press 'q' to exit.")
acq_camera.get_img()