### COVID-19 Cases Prediction
* Given survey results in the past 3 days in a specific state in U.S., then
predict the percentage of new tested positive cases in the 3rd day.
* Other detailed information can be check in the **HW01.pdf**

### Targets 
* Solve a regression problem with deep neural networks (DNN).
* Basic DNN training tips
* Realize the effects of hyperparameters (e.g. batch_size, regularization, learning rate, optimizer)

### Implementation (2021/10/1)
* Based on TA' source code and make some improvements
* The approaches I had tried and tuned:
  * Feature Extraction with SelectKBest
  * Add L2 regularization
  * Tuned hyperparameters (optimizers, learning rate, batch size...)
  * Tuned structure of DNN (dropout, batch normaliztion, activation function, layer...)
### Result
Since the criterion is based on the RMSE, the smaller error stands for the better performance of prediction.
Professor had set the simple/medium/strong baseline to judge our model.
* Baseline (Public/Private)
  * Strong: 0.88017/0.89266
  * Medium: 1.28359/1.36937 
  * Simple: 2.03004/2.04826
* My result: (0.88153/0.89477)
* The results are still slight worse than strong baseline.
---
### Review & Retry (2022/5/10)
This time, I had modified and re-tuned the hyperparameters based on previous trials and much deeper understanding of ML. The code is shown in the **COVID_19_Prediction_v2.ipynb**.
* **Modification :**
  * MSE $\rightarrow$ RMSE
* **Feature Extraction**
  * Selected useful features with ***SelectBest***
  * Tuned the number of features. 
* **Hyperparameters Tuning:**
  * Ratio of training/validation dataset = 15:1 ~ 20:1
  * Batch_size = 16, 32, 64, 256, 512
  * Optimizer = SGD, Adam, AdamW
    * Learning rate = 0.00005 ~ 0.005
    * weight_decay (L2 regularization) : 0.0005 ~ 0.005
 * **DNN structure:**
   * Number of layer(s) = 1, 2
   * dropout: 0.1 ~ 0.5
   * batch_normalization
   * activation function: Sigmoid, ReLU, LeakyReLU(0.1~0.5), SELU
   * neurons in hidden layers: 16, 32, 64, 128

***Final Result:***

Result: 0.87831/0.89132 (pass strong baseline (0.88017/0.89266))
<img src="https://i.imgur.com/rXGpYh4.png" width=60%>
