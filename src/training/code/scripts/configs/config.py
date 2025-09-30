import torch

checkpoint = "Salesforce/codet5p-220m-py"
batch_size = 16
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")