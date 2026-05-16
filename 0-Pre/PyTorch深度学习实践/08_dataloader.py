'''
Author: mazezen
Date: 2026-05-16
LastEditors: mazezen
LastEditTime: 2026-05-16
FilePath: /ailearning/0-Pre/PyTorch深度学习实践/08_dataloader.py
Description: PyTorch 深度学习实践 加载数据集ß
'''

import torch
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split

print('数据集文件: diabetes.csv')

# 读取数据集信息
raw_data = np.loadtxt('diabetes.csv', delimiter=',', dtype=np.float32)
print(f'数据集形状: {raw_data.shape}')
print(f'特征数量: {raw_data.shape[1]-1}')
print(f'样本数量: {raw_data.shape[0]}')

# prepare dataset
class DiabetesDataset(Dataset):
    def __init__(self, filepath):
        xy = np.loadtxt(filepath, delimiter=',', dtype=np.float32)
        self.len = xy.shape[0]
        self.x_data = torch.from_numpy(xy[:, :-1])
        self.y_data = torch.from_numpy(xy[:, [-1]])
        print(f'数据集加载完成, 样本数: {self.len}')

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
        
    def __len__(self):
        return self.len
    
# 创建数据集
dataset = DiabetesDataset('diabetes.csv')
train_loader = DataLoader(dataset=dataset, batch_size=32, shuffle=True, num_workers=0) # num_works 多线程

class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x
    
model = Model()

criterion = torch.nn.BCELoss(reduction='mean')
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

print('\n开始训练(基础版本)...')
print('训练参数: ')
print(f'- 批量大小: 32')
print(f'- 学习率: 0.01')
print(f'- 损失函数: BCELoss')
print(f'- 优化器: SGD')

if __name__ == '__main__':
    # 基础版训练. 只训练10个 epoch 用于演示ß
    for epoch in range(10): 
        for i, data in enumerate(train_loader, 0):
            inputs, labels = data
            y_pred = model(inputs)
            loss = criterion(y_pred, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if i % 10 == 0:
                print(f'Epoch: {epoch}, Batch: {i}, Loss: {loss.item():.4f}')

print('划分训练集和测试集...')
X = raw_data[:, :-1]
y = raw_data[:, [-1]]
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=0.3)
Xtest = torch.from_numpy(Xtest)
Ytest = torch.from_numpy(Ytest)

print(f'训练集大小: {Xtrain.shape[0]}')
print(f'测试集大小: {Xtest.shape[0]}')

# 将训练数据集进行批量处理
class DiabetesDatasetV2(Dataset):
    def __init__(self, data, label):
        self.len = data.shape[0]
        self.x_data = torch.from_numpy(data)
        self.y_data = torch.from_numpy(label)
    
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    
    def __len__(self):
        return self.len
    
train_dataset = DiabetesDatasetV2(Xtrain, Ytrain)
train_loader_v2 = DataLoader(dataset=train_dataset, batch_size=32, shuffle=True, num_workers=0)

class ModelV2(torch.nn.Module):
    def __init__(self):
        super(ModelV2, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x
    
model_v2 = ModelV2()
    
# construct loss and optimizer
criterion_v2 = torch.nn.BCELoss(reduction='mean')
optimizer_v2 = torch.optim.SGD(model_v2.parameters(), lr=0.01)

# training cycle forward, backward, update
def train(epoch):
    train_loss = 0.0
    count = 0
    for i, data in enumerate(train_loader_v2, 0):
        inputs, labels = data
        y_pred = model_v2(inputs)
        loss = criterion_v2(y_pred, labels)
        optimizer_v2.zero_grad()
        loss.backward()
        optimizer_v2.step()
        train_loss += loss.item()
        count = i
    
    if epoch % 5 == 4: # 每 5 个 epoch打印一次
        print(f'Epoch: {epoch}, Batch: {i}, Loss: {loss.item():.4f}')

def test():
    with torch.no_grad():
        y_pred = model_v2(Xtest)
        y_pred_label = torch.where(y_pred >= 0.5, torch.tensor([1.0]), torch.tensor([0.0]))
        acc = torch.eq(y_pred_label, Ytest).sum().item() / Ytest.size(0)
        print(f'Test Accuracy: {acc:.4f}')

print('\n开始训练(扩展版本)...')
# 只训练20个 epoch用于演示
for epoch in range(20):
    train(epoch=epoch)
    if epoch % 5 == 4:
        test()

print('\n' + '='*50)
print("数据加载信息: ")
print('='*50)
print(f'训练集样本数: {len(train_dataset)}')
print(f'批量大小: 32')
print(f'每个 epoch 的 batch 的数: {len(train_loader_v2)}')
print(f'特征维度: 8')
print(f'标签未读: 1')

print(f'\n演示完成!')
