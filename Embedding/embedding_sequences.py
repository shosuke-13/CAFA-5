# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
import time
import numpy as np
import torch
from transformers import BertModel, BertTokenizer
from tqdm import tqdm
from Bio import SeqIO


# use biopython to extract protein properties
train_fn = "./Train/train_sequences.fasta"
test_fn = "./Test (Targets)/testsuperset.fasta"

# use mac GPU
device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')
tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert", do_lower_case=False )
model = BertModel.from_pretrained("Rostlab/prot_bert").to(device)

# clip the first 100 symbols of each sequence
clip_first_n_symbols=100


def tokenize_sequences(sequences):
    emb_list=[]
    id_list=[]
    t00 = time.time()

    for seq in tqdm(sequences):
        sequence_example = seq[:clip_first_n_symbols]
        sequence_example = ' '.join(list(sequence_example))

        encoded_input = tokenizer(sequence_example, return_tensors='pt').to(device)
        output = model(**encoded_input)   
        id_list.append(seq.id)
        emb_list.append(output['last_hidden_state'][:,0][0].detach().cpu().numpy())

    print('Time:',time.time()-t00)
    return np.array(id_list), np.array(emb_list)


if __name__ == "__main__":
    # execute only if run as a script
    set_sequences = [SeqIO.parse(train_fn, "fasta"), SeqIO.parse(test_fn, "fasta")]

    for i, sequences in enumerate(set_sequences):
        # Train sequences embeddings
        if i == 0:
            id, emb = tokenize_sequences(sequences)
            np.save('train_ids.npy', id)
            np.save('train_embeddings.npy', emb)

        # Test sequences embeddings
        else:
            id, emb = tokenize_sequences(sequences)
            np.save('test_ids.npy', id)
            np.save('test_embeddings.npy', emb)   