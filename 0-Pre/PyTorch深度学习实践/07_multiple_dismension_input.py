'''
Author: mazezen
Date: 2026-05-16
LastEditors: mazezen
LastEditTime: 2026-05-16
FilePath: /ailearning/0-Pre/PyTorch深度学习实践/07_multiple_dismension_input.py
Description: PyTorch 深度学习实践 - 处理多维特征的输入
'''

import torch
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
plt.rcParams['axes.unicode_minus'] = False


class DiabetesDataset:
    '''糖尿病数据集分类'''

    def __init__(self, csv_path='diabetes.csv'):
        self.csv_path = csv_path
        self.load_data()

    def load_data(self):
        '''加载糖尿病数据集'''
        try:
            if not Path(self.csv_path).exists():
                print(f'警告: {self.csv_path} 不存在, 创建模拟数据集...')
                self.create_mock_dataset()

            xy = np.loadtxt(self.csv_path, delimiter=',', dtype=np.float32)
            self.x_data = torch.from_numpy(xy[:, :-1])
            self.y_data = torch.from_numpy(xy[:, [-1]])
            print(f'数据集加载成功: {self.x_data.shape[0]} 个样本, {self.x_data.shape[1]} 个特征')
        except Exception as e:
            print(f'加载数据集失败: {e}')
            self.create_mock_dataset()

    def create_mock_dataset(self):
        '''创建模拟糖尿病数据集'''
        np.random.seed(42)
        n_samples = 768

        # 创建8个特征
        features = np.random.randn(n_samples, 8)

        # 创建标签(二分类)
        labels = (np.random.rand(n_samples, 1) > 0.5).astype(np.float32)

        # 保存为 CSV 文件
        data = np.column_stack([features, labels])
        np.savetxt(self.csv_path, data, delimiter=',', fmt='%.6f')

        print(f'已创建模拟数据集: {self.csv_path}')


class DiabetesModel(torch.nn.Module):
    def __init__(self, input_dim=8, hidden1=6, hidden2=4, output_dim=1):
        super(DiabetesModel, self).__init__()
        self.linear1 = torch.nn.Linear(input_dim, hidden1)
        self.linear2 = torch.nn.Linear(hidden1, hidden2)
        self.linear3 = torch.nn.Linear(hidden2, output_dim)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        return x


class DiabetesTrainer:
    '''糖尿病训练器'''

    def __init__(self, model, learning_rate=0.1):
        self.model = model
        self.criterion = torch.nn.BCELoss(reduction='mean')
        self.optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
        self.epoch_list = []
        self.loss_list = []

    def train(self, x_data, y_data, epochs=100):
        print(f'开始训练, 共{epochs} 个 epoch...')

        for epoch in range(epochs):
            y_pred = self.model(x_data)
            loss = self.criterion(y_pred, y_data)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            if epoch % 10 == 0:
                print(f'Epoch [{epoch}/{epochs}], Loss: {loss.item():.4f}')

            self.epoch_list.append(epoch)
            self.loss_list.append(loss.item())

    def evaluate(self, x_data, y_data):
        '''评估模型性能'''
        self.model.eval()
        with torch.no_grad():
            y_pred = self.model(x_data)
            y_pred_label = torch.where(y_pred >= 0.5,
                                       torch.tensor([1.0]),
                                       torch.tensor([0.0]))
            accuracy = torch.eq(y_pred_label, y_data).sum().item() / y_data.size(0)
            print(f'模型准确率: {accuracy:.4f}')
            return accuracy

    def plot_training_loss(self):
        '''绘制训练损失曲线'''
        plt.figure(figsize=(10, 6))
        plt.plot(self.epoch_list, self.loss_list)
        plt.title('训练损失曲线')
        plt.xlabel('Epoch')
        plt.ylabel('Loss')
        plt.grid(True)
        plt.savefig('training_loss.png')
        plt.show()

    def print_model_parameters(self):
        '''打印模型参数'''
        print('\n=== 模型参数 ===')
        layer1_weight = self.model.linear1.weight.data
        layer1_bias = self.model.linear1.bias.data

        print('第一层权重 shape: ', layer1_weight.shape)
        print('第一层偏置 shape: ', layer1_bias.shape)
        print('第一层权重 (前5个值): ', layer1_weight[0][:5])
        print('第一层偏置 (第一个值): ', layer1_bias[0])


class ExtendDiabetesModel(torch.nn.Module):
    '''扩展糖尿病预测模型(4层网络)'''

    def __init__(self, input_dim=8):
        super(ExtendDiabetesModel, self).__init__()
        self.linear1 = torch.nn.Linear(input_dim, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 2)
        self.linear4 = torch.nn.Linear(2, 1)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x):
        x = self.sigmoid(self.linear1(x))
        x = self.sigmoid(self.linear2(x))
        x = self.sigmoid(self.linear3(x))
        x = self.sigmoid(self.linear4(x))
        return x


def main():
    # 1. 加载数据
    dataset = DiabetesDataset('diabetes.csv')
    x_data, y_data = dataset.x_data, dataset.y_data

    # 2. 创建基础模型
    print('\n--- 基础3层网络模型 ---')
    model = DiabetesModel()
    trainer = DiabetesTrainer(model=model)

    # 3. 训练基础模型
    trainer.train(x_data=x_data, y_data=y_data, epochs=100)
    trainer.plot_training_loss()
    trainer.evaluate(x_data, y_data)
    trainer.print_model_parameters()

    # 4. 创建扩展模型
    print('\n--- 扩展4层网络模型 ---')
    extended_model = ExtendDiabetesModel()
    extended_trainer = DiabetesTrainer(extended_model)
 
    # 5. 训练扩展模型
    extended_trainer.train(x_data, y_data, epochs=1000)
    extended_trainer.evaluate(x_data, y_data)

    # 6. 保存模型
    torch.save(model.state_dict(), 'diabetes_model.pth')
    torch.save(extended_model.state_dict(), 'diabetes_extended_model.pth')
    print(f'\n模型已保存: diabetes_model.pth, diabetes_extended_model.pth')


if __name__ == '__main__':
    main()
