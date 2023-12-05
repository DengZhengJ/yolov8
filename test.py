# 输入库
import torch
# 查看版本
print(torch.__version__)

# 查看gpu是否可用
print(torch.cuda.is_available())

# 查看对应CUDA的版本号
print(torch.backends.cudnn.version())
print(torch.version.cuda)

# 退出python   yolo task=detect mode=predict model=yolov8n.pt conf=0.25 source='ultralytics/assets/bus.jpg
quit()