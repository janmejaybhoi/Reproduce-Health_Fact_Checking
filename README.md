# Reproducibility of Explainable Automated Fact-Checking for Public Health Claims

This repository is the implementation of [Explainable Automated Fact-Checking for Public Health Claims](https://arxiv.org/abs/2010.09926). Also, this is the submission of our work under the ML Reproducibility Challenge 2021 Spring.
The repository reproduces the veracity prediction as mentioned in the paper with BERT(base-uncased) and Sci-BERT models. We acheive accuracy close to that mentioned in the paper.

The repository also reproduces explanation generation for each claim with Bart(DistillBart) pretrained on CNN-Daily Mail dataset. We achieved better rouge scores than what is mentioned in the paper

## Requirements

To install requirements:

```setup
pip install -r requirements.txt
```

## Train model for veracity prediction

To train the BERT or Sci-BERT models for veracity prediction. Fork and clone this GitHub Repository in your local environment.

```setup
git clone repository
```

Go to the veracity_prediction_bert-base or veracity_prediction_scibert folder

```setup
cd veracity_prediction_bert-base
```

OR

```setup
cd veracity_prediction_scibert
```

Open the config.py([bert-base-uncased](https://github.com/saswat01/Reproduce-Health_Fact_Checking/blob/main/veracity_prediction_bert-base/config.py), [scibert](https://github.com/saswat01/Reproduce-Health_Fact_Checking/blob/main/veracity_prediction_scibert/config.py)) file. Make sure to make an empty folder/directory inside the bert or scibert directory for saving the checkpoints. You should provide this checkpoint path in the config.py file. Also, hyper parameters like learning rate, epochs, batch size have been set to the best results but can be changed to preform experiment. Change the training, validation and test directory path to match your requirements(please use the [processed](https://github.com/saswat01/Reproduce-Health_Fact_Checking/tree/main/data/processed) data we have provided in the repository).

After deciding your parameters and changing path to data directories run the following to train your model:

```setup
python veracity_prediction_bert-base/train.py
```

OR

```setup
python veracity_prediction_scibert/train.py
```

## Metrics for veracity prediction

For displaying metrics run:

BERT

```setup
python veracity_prediction_bert-base/metrics.py
```

Sci-BERT

```bash
python veracity_prediction_scibert/metrics.py
```

## Results

### BERT RESULTS

BERT model acheives a test accuracy of 63.40% on test dataset with parameters *batch_size=10*, *learning_rate=1e-6* and *epochs=4*. Our model was trained on Google Colab with Nvidia T4 GPU.

You can have a look at the bert models classification report below {0:False, 1:True, 2:Mixture, 3:Unproven}:

<img src ="https://github.com/saswat01/Reproduce-Health_Fact_Checking/blob/main/veracity_prediction_bert-base/bert_result.png" alt="bert_classification_report">

|class/ metric| precision | recall  | f1-score | support |
|-------------| --------- |-------- | -------- |---------|
|False        | 0.51      |  0.77   |    0.61  | 388     |  
|True         | 0.75      |  0.80   |    0.77  | 599     |
|Mixture      | 0.14      |  0.00   |    0.01  | 201     |
|Unproven     | 0.00      |  0.00   |    0.00  | 45      |
|macro avg    | 0.35      | 0.39    |    0.35  |         | 
|weighted avg | 0.55      | 0.63    |    0.57  |         | 

#### Sci-BERT RESULTS

Sci-Bert model ahceives a test accuracy of 64% with the *batch_size=13* and *epochs=5* and *learning_rate=1e-6* same as the ones used for the BERT model. This model was also trained on Google Colab with Nvidia T4 GPU.

Classification report for Sci-BERT {0:False, 1:True, 2:Mixture, 3:Unproven}:

<img src ="https://github.com/saswat01/Reproduce-Health_Fact_Checking/blob/main/veracity_prediction_scibert/scibert2_results.png" alt="sci-bert_classification_report">

|class/ metric| precision | recall  | f1-score | support |
|-------------| --------- |-------- | -------- |---------|
|False        | 0.54      |  0.77   |    0.61  | 388     |  
|True         | 0.70      |  0.81   |    0.76  | 599     |
|Mixture      | 0.50      |  0.04   |    0.08  | 201     |
|Unproven     | 0.00      |  0.00   |    0.00  | 47      |
|macro avg    | 0.44      | 0.39    |    0.36  |         |
|weighted avg | 0.60      | 0.64    |    0.57  |         |

## Extractive and Abstractive Summarization

To verify the veracity prediction an extractive abstractive summarization can also be generated against explanation for each claim. As given in the paper, We used model pretrained on CNN daily-mail dataset from huggingface models library. The Model was trained on Top_k sentences we got while performing cosine similarity between sentences in main_text and claim. For training we used *lr=5e-5*, *batch_size=8* and *epochs=3*. The training was done in google colab environment on Nvidia T4 GPU. The model was tested using rouge score on test data. The results were

|    Metric   | precision | recall  | f1-score |
|-------------| --------- |-------- | -------- |
|      R1     | 0.459     |  0.438  |    0.447 |
|      R2     | 0.165     |  0.158  |    0.161 |
|      RL     | 0.395     |  0.377  |    0.385 |

To train the model on dataset you can use this command

```bash
python Explanation_Summarization/train.py --model='bart'
```

If you want to save the model after training you can do it by providing additional arguments

```bash
python Explanation_Summarization/train.py --model='bart' --epochs=4 --save_model=True --model_path='path'
```

You can evaluate the trained model on test data. You can provide the path to test data in config file

```bash
python Explanation_Summarization/eval.py --path="Path to the model checkpoint"
```
## Fine-tuned models

We have made the fine-tuned models available on [Google Drive](https://drive.google.com/drive/folders/1-J89aDK4zy2_1ln1Jxz7YaWPVAXfPp6t?usp=sharing) which can be downloaded and used directly.

## Testing

To test the model either you can use the test dataset or can provide claim, main_text and the script will predict the veracity and generate explanation using the fine tuned models.

```bash
python test.py --claim="claim sentence" --main_text="text describing claim sentence"
```

If you don't provide claim and main_text arguments, script will randomly pick a claim sentence and corresponding main_text from test dataset and output veracity prediction and explanation.
## References

```
@inproceedings{kotonya-toni-2020-explainable,
    title = "Explainable Automated Fact-Checking for Public Health Claims",
    author = "Kotonya, Neema  and
      Toni, Francesca",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP)",
    month = nov,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-main.623",
    pages = "7740--7754",
}
```
