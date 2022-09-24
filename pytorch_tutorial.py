import torch

x = torch.rand(2, 2)
y = torch.rand(2, 2)

# every function that has an underscore will do an in-place operation
y.add_(x)
print(y)

# Division 
z = x / y
z = torch.div(x, y)

# This creates a random tensor of dimensions 5 * 3
x = torch.rand(5, 3)

# Slicing
# This prints for all of the rows, but only the first column (index 0)
print(x[:, 0])

# This prints for all of the columns, but only the first row (index 1)
print(x[1, :])

# Obtain a singular element within the tensor
print(x[1, 1])

# Obtains the actual value
print(x[1, 1].item())

# Reshaping a tensor
x = torch.rand(4, 4)
print(x)

# Reshapes our tensor to a one-dimensional vector
y = x.view(16)
print(y)



