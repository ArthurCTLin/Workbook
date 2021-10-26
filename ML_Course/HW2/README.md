### Targets 
  * Basic understanding of Speech recognition
  * Solve a classification task with DNN
  * Get familiar with PyTorch.
### Task description
* Framewise phoneme prediction from speech
* Given a dataset preprocessed (Acoustic Features - MFCCs ) by TA and the labels of corresponding phoneme.
One should train a DNN model with the train dataset and lables, and then classify the speech frames of the testing dataset into the correct phoneme.
* Other detailed information can be check in the **HW02.pdf**
### Implementation
* Based on TA' source code and make some improvements
* The approaches I had tried and tuned:
  * Increased the hidden layers of DNN model
  * Tuned the dim in the hidden layers
  * Tuned hyperparameters (optimizers, learning rate, batch size...)
  * Tuned structure of DNN (dropout, batch normaliztion, activation function, layer...)
  * Two steps of training :
    *  500 epochs with lr=1.00E-04 (Save the model as HW2_28_model.ckpt)
    *  200 epochs with lr=1.00E-06
### Result
* Public: 0.74694, Private: 0.74678 (Strong Baseline for Public/Private: 0.76023/0.76118)
* The results are still slight worse than strong baseline. 
* I will temporarily continue to other HWs and update the result of this assignment while finding out the methods improving the model. 
