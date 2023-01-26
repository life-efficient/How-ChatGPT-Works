from torch.utils.data import DataLoader

def collate_fn(batch):
    print(batch)
    sequences = [preprocess_text(b["text"]) for b in batch]
    sequences.sort(key=lambda seq : -len(seq))
    labels = torch.tensor([b["feeling"] for b in batch])

    padded_sequences = torch.nn.utils.rnn.pad_sequence(sequences)
    # print(padded_sequences)
    # print(padded_sequences.shape)
    packed_padded_seqs = torch.nn.utils.rnn.pack_padded_sequence(padded_sequences, lengths=[len(seq) for seq in sequences])
    # print(packed_padded_seqs)
    return packed_padded_seqs, labels

train_loader = DataLoader(train_set, batch_size=4, collate_fn=collate_fn)

for batch in train_loader:
    print(batch)
    break


# %%
import torch
import torch.nn.functional as F
from torch.utils.tensorboard import SummaryWriter

def train(model, dataloader, epochs=10):

  # INITIALISE TRACKING
  writer = SummaryWriter()
  batch_idx = 0

  optimiser = torch.optim.SGD(model.parameters(), lr=0.01) # Define optimiser and set learning rate
  
  for epoch in range(epochs):# a number of times
    for example in dataloader: # iterate throguh the dataset
      
      # UNPACK EXAMPLE
      tweets, sentiments = example
      
      # MAKE PREDICTION
      prediction = model(tweets) # make prediction
      
      # CALCULATE LOSS
      loss = F.binary_cross_entropy(prediction.squeeze(), sentiments) # calculate loss
      
      # CALCULATE GRADIENTS
      loss.backward()
      
      # MOVE PARAMETERS
      optimiser.step()

      # ZERO GRAD
      optimiser.zero_grad()

      # TRACK PROGRESS
      writer.add_scalar("Train/Loss", loss.item(), batch_idx)
      batch_idx += 1

rnn = RNN(vocab_size, hidden_size=128, num_layers=2)
train(rnn, train_loader)