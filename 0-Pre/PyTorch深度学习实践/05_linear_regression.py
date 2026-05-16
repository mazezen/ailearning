'''
Author: mazezen
Date: 2026-05-16
LastEditors: mazezen
LastEditTime: 2026-05-16
FilePath: /ailearning/0-Pre/PyTorch深度学习实践/05_linear_regression.py
Description: PyTorch 深度学习实践 Linear Regression
'''

from typing import Any

import torch

x_data = torch.tensor([[1.0], [2.0], [3.0]])
y_data = torch.tensor([[2.0], [4.0], [6.0]])


class LinearModel(torch.nn.Module):
    def __init__(self) -> None:
        super(LinearModel, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred
    
model = LinearModel()

crierion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

for epoch in range(100):
    y_pred = model(x_data)
    loss = crierion(y_pred, y_data)
    print(epoch, loss.item())

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print('w= ', model.linear.weight.item())
print('b= ', model.linear.bias.item())

x_test = torch.tensor([[4.0]])
y_test = model(x_test)
print('y_pred= ', y_test.data)
