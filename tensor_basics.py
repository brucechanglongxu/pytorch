import torch
import numpy as np

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

# If we take -1 as an input, then pytorch will automatically set the appropriate size
y = x.view(-1, 8)
print(y.size())

# Converting a tensor into a numpy array
# Caution, if this model is on the CPU instead of the GPU
# then changing b will also change a. Note that Numpy can only handle CPU tensors
# so if we move our tensor to the GPU, we should move it back to the CPU in order to
# convert back from a tensor to a numpy array
a = torch.ones(5) 
print(a)
b = a.numpy()
print(b)

# check if CUDA is available
if torch.cuda.is_available():
  device = torch.device("cuda")
  # This will create a tensor and create it on the GPU
  x = torch.ones(5, device=device)
  # This creates a tensor on the CPU and then moves it to the GPU
  y = torch.ones(5)
  y = y.to(device)
  z = x + y 
  
