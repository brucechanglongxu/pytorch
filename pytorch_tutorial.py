import torch

x = torch.rand(2, 2)
y = torch.rand(2, 2)

# every function that has an underscore will do an in-place operation
y.add_(x)
print(y)

x = torch.rand(5, 3)

# This prints for all of the rows, but only the first column (index 0)
print(x[:, 0])

