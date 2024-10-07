from sklearn.ensemble import IsolationForest
import numpy as np

def clean_missing_values(data):
  return data.drop(['temp', 'rawState'], axis=1)

def reset_index(data):
  return data.reset_index(drop=True)

def remove_outliers(data):  
  remove_non_numeric = data.drop(['state', 'filename'], axis=1)
  clf = IsolationForest(n_estimators=10)
  outliers = clf.fit_predict(remove_non_numeric)
  data = reset_index(data)
  return data.drop(np.where(outliers == -1)[0])

def remove_state_outliers(data):
  states = ['w', 'r', 'n']
  return data[data.state.isin(states)]


def rem_nrem_data(data):
  return data[data.state != 'w']

def wake_sleep_data(data):
  return data.replace({'state': {'n': 's', 'r': 's'}})

def do_preprocessing(data, mode=None):  
  data = clean_missing_values(data)
  data = remove_state_outliers(data)

  if(mode == "RN"):    
    data = rem_nrem_data(data)
  elif(mode == "WS"):
    data = wake_sleep_data(data)

  data = remove_outliers(data)
  return data

def transform_state_to_binary(data, mode=None):
  if(mode == "RN"):    
    return data.replace({'state': {'n': 0, 'r': 1}})
  elif(mode == "WS"):
    return data.replace({'state': {'n': 0, 'r': 1}})
  return data.replace({'state': {'n': 0, 'r': 0.5, 'w': 1}})