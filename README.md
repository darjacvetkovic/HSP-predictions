# Hansen solubility parameter (HSP) predictions 
 XGBoost and GNN training and models for prediction of Hansen solubility parameters for an upcoming paper.

Folders:
 - `data` : folder with all data used in the paper
 - `trained_models`: folder with trained models, for now only XGBOOST models are available in GitHub (due to their size), if you want to use trained GNN models download them from this [link](https://drive.google.com/drive/folders/1JqV2n3172aHr_v6qGoITSJl9H30riOh-?usp=drive_link).

Files:

_XGBOOST related_

 - `XGBOOST_feature_generation.ipynb` - jupyter notebook with the code for generating descriptors(features) for the molecues, along with their initial filtering
 - `XGBOOST_training.ipynb` - jupyter notebook for training and testing XGBOOST models
 - `XGBOOST_new_data_predictions.ipynb` - jupyter notebook for loading and applying/testing the XGBOOST models on new data
   
_GNN related_

- `GNN_training_D/P/H.ipynb` - jupyter notebook for training the GNN models for D(dispersive component), P(polar component) or H(hydrogen bond component) parameter. They are separate for readability purposes, but the code is essentialy the same in all three cases.
- `GNN_new_data_predictions.ipynb` - jupyter notebook for loading and applying/testing the GNN models on new data. Make sure you download the models from the above link first and put them in a convinient folder (in the notebook it's in the trained_models/gnn but it's not neceserry, just change the `model_dir` argument to the appropriate path)
