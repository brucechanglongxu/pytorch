import torch

x = torch.rand(2, 2)
y = torch.rand(2, 2)

# every function that has an underscore will do an in-place operation
y.add_(x)
print(y)
