import torch

x = torch.rand(2, 2)
y = torch.rand(2, 2)

# every function that has an underscore will do an in-place operation
y.add_(x)
print(y)

# This creates a random tensor of dimensions 5 * 3
x = torch.rand(5, 3)

# This prints for all of the rows, but only the first column (index 0)
print(x[:, 0])

# This prints for all of the columns, but only the first row (index 1)
print(x[1, :])

# Reshaping a tensor
x = torch.rand(4, 4)
print(x)

# Reshapes our tensor to a one-dimensional vector
y = x.view(16)
print(y)



