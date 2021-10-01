### Targets 
* Solve a regression problem with deep neural networks (DNN).
* Basic DNN training tips
* Get familiar with PyTorch
### Task description
* COVID-19 Cases Prediction
* Given survey results in the past 3 days in a specific state in U.S., then
predict the percentage of new tested positive cases in the 3rd day.
* Other detailed information can be check in the **HW01.pdf**
### Implementation
* Based on TA' source code and make some improvements
* The approaches I had tried and tuned:
  * Feature Extraction with SelectKBest
  * Add L2 regularization
  * Tuned hyperparameters (optimizers, learning rate, batch size...)
  * Tuned structure of DNN (dropout, batch normaliztion, activation function, layer...)
### Result
* Public: 0.88153, Private: 0.89477 (Strong Baseline for Public/Private: 0.88017/0.89266)
* The results are still slight worse than strong baseline. 
(However, in order not to get a biased model, I just stopped while there is no obvious overfitting  issue.)
