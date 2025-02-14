import numpy as np

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Subtract max for numerical stability
    return exp_x / np.sum(exp_x)

# Example usage:
logits = np.array([2.0, 1.0, 0.1])
softmax_output = softmax(logits)

print("Softmax Output:", softmax_output)
