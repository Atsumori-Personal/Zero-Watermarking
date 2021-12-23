import numpy as np

def ber(a, b):
    Height = a.shape[0]
    Width = a.shape[1]

    correct = 0

    for i in range(Height):
        for j in range(Width):
            if a[i,j] == b[i,j]:
                correct += 1
    
    return correct / (Height * Width)