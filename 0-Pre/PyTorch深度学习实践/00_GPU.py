'''
Author: mazezen
Date: 2026-05-16
LastEditors: mazezen
LastEditTime: 2026-05-16
FilePath: /ailearning/0-Pre/PyTorch深度学习实践/00_GPU.py
'''

import torch

# print(torch.__version__)

# ================================================================
#                        USE GPU                                 #
# ================================================================

# NVIDIA 'CUDA'
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# Apple Silicon GPC PyTorch>=v.12 MPS(Metal Performance Shaders)
if torch.backends.mps.is_available() and torch.backends.mps.is_built():
    device = torch.device('mps')
    print("GPU (MPS) 加速已启用")
else:
    device = torch.device("cpu")
    print("GPU 不可用, 使用CPU")
