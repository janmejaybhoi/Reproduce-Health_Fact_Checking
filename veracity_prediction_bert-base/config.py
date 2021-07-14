import transformers
from transformers import BertTokenizerFast as BertTokenizer, BertModel, AdamW, get_linear_schedule_with_warmup

MAX_LEN = 512 # max number of tokens in a sentence
N_EPOCHS = 4 # number of epochs
BATCH_SIZE = 10 # batch size of train, eval is same
CHECKPOINT_PATH = '' #save model checkpoints in this folder
N_CLASSES = 4
LEARNING_RATE = 1e-6 # learning rate

TOKENIZER = BertTokenizer.from_pretrained('bert-base-uncased') # bert base uncased tokenizer for fine-tuning

TRAINING_FILE = '' # train data path (use the processed folder in data folder of this repository)
VALIDATION_FILE = '' # validation data path (use the processed folder in data folder of this repository)
TESTING_FILE = '' # test data path (use the processed folder in data folder of this repository)
