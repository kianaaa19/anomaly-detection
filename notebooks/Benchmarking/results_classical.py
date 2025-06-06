IEEE_CIS_AE = {
  '0': {'precision': 0.80, 'recall': 0.90, 'f1-score': 0.85, 'support': 569877},
  '1': {'precision': 0.58, 'recall': 0.38, 'f1-score': 0.46, 'support': 206630},
  'accuracy': 0.76,
  'macro avg': {'precision': 0.69, 'recall': 0.64, 'f1-score': 0.65, 'support': 776507},
  'weighted avg': {'precision': 0.74, 'recall': 0.76, 'f1-score': 0.74, 'support': 776507}
}

IEEE_CIS_IF = {
  '0': {'precision': 0.80, 'recall': 0.90, 'f1-score': 0.85, 'support': 569877},
  '1': {'precision': 0.59, 'recall': 0.40, 'f1-score': 0.48, 'support': 206630},
  'accuracy': 0.77,
  'macro avg': {'precision': 0.70, 'recall': 0.65, 'f1-score': 0.66, 'support': 776507},
  'weighted avg': {'precision': 0.75, 'recall': 0.77, 'f1-score': 0.75, 'support': 776507}
}

IEEE_CIS_OSVM = {
  '0': {'precision': 0.98, 'recall': 0.90, 'f1-score': 0.93, 'support': 569877},
  '1': {'precision': 0.13, 'recall': 0.41, 'f1-score': 0.20, 'support': 206630},
  'accuracy': 0.77,
  'macro avg': {'precision': 0.70, 'recall': 0.65, 'f1-score': 0.66, 'support': 776507},
  'weighted avg': {'precision': 0.75, 'recall': 0.77, 'f1-score': 0.75, 'support': 776507}
}

ISCOM_AE = {
  '0': {'precision': 0.65, 'recall': 0.64, 'f1-score': 0.64, 'support': 1463},
  '1': {'precision': 0.50, 'recall': 0.51, 'f1-score': 0.50, 'support': 1040},
  'accuracy': 0.58,
  'macro avg': {'precision': 0.57, 'recall': 0.57, 'f1-score': 0.57, 'support': 2503},
  'weighted avg': {'precision': 0.58, 'recall': 0.58, 'f1-score': 0.58, 'support': 2503}
}

ISCOM_IF = {
  '0': {'precision': 0.62, 'recall': 0.80, 'f1-score': 0.70, 'support': 1463},
  '1': {'precision': 0.54, 'recall': 0.32, 'f1-score': 0.40, 'support': 1040},
  'accuracy': 0.60,
  'macro avg': {'precision': 0.58, 'recall': 0.56, 'f1-score': 0.55, 'support': 2503},
  'weighted avg': {'precision': 0.59, 'recall': 0.60, 'f1-score': 0.58, 'support': 2503}
}

ISCOM_OCSVM = {
  '0': {'precision': 0.63, 'recall': 0.81, 'f1-score': 0.71, 'support': 1463},
  '1': {'precision': 0.56, 'recall': 0.34, 'f1-score': 0.42, 'support': 1040},
  'accuracy': 0.61,
  'macro avg': {'precision': 0.59, 'recall': 0.57, 'f1-score': 0.57, 'support': 2503},
  'weighted avg': {'precision': 0.60, 'recall': 0.61, 'f1-score': 0.59, 'support': 2503}
}

NSL_KDD_IF = {
  '0': {'precision': 0.76, 'recall': 0.91, 'f1-score': 0.82, 'support': 9711},
  '1': {'precision': 0.92, 'recall': 0.78, 'f1-score': 0.84, 'support': 12833},
  'accuracy': 0.83,
  'macro avg': {'precision': 0.84, 'recall': 0.84, 'f1-score': 0.83, 'support': 22544},
  'weighted avg': {'precision': 0.85, 'recall': 0.83, 'f1-score': 0.84, 'support': 22544}
}

NSL_KDD_AE = {
  '0': {'precision': 0.65, 'recall': 0.88, 'f1-score': 0.75, 'support': 9711},
  '1': {'precision': 0.88, 'recall': 0.64, 'f1-score': 0.74, 'support': 12833},
  'accuracy': 0.75,
  'macro avg': {'precision': 0.77, 'recall': 0.76, 'f1-score': 0.75, 'support': 22544},
  'weighted avg': {'precision': 0.78, 'recall': 0.75, 'f1-score': 0.75, 'support': 22544}
}

NSL_KDD_OCSVM = {
  '0': {'precision': 0.78, 'recall': 0.88, 'f1-score': 0.83, 'support': 9711},
  '1': {'precision': 0.90, 'recall': 0.81, 'f1-score': 0.85, 'support': 12833},
  'accuracy': 0.84,
  'macro avg': {'precision': 0.84, 'recall': 0.85, 'f1-score': 0.84, 'support': 22544},
  'weighted avg': {'precision': 0.85, 'recall': 0.84, 'f1-score': 0.84, 'support': 22544}
}


classical_models_results = [
    # IEEE_CIS classical models
    [
        {'Label 0': IEEE_CIS_AE['0'], 'Label 1': IEEE_CIS_AE['1']},
        {'Label 0': IEEE_CIS_IF['0'], 'Label 1': IEEE_CIS_IF['1']},
        {'Label 0': IEEE_CIS_OSVM['0'], 'Label 1': IEEE_CIS_OSVM['1']},
    ],
    # ISCOM classical models
    [
        {'Label 0': ISCOM_AE['0'], 'Label 1': ISCOM_AE['1']},
        {'Label 0': ISCOM_IF['0'], 'Label 1': ISCOM_IF['1']},
        {'Label 0': ISCOM_OCSVM['0'], 'Label 1': ISCOM_OCSVM['1']},
    ],
    # NSL-KDD classical models
    [
        {'Label 0': NSL_KDD_AE['0'], 'Label 1': NSL_KDD_AE['1']},
        {'Label 0': NSL_KDD_IF['0'], 'Label 1': NSL_KDD_IF['1']},
        {'Label 0': NSL_KDD_OCSVM['0'], 'Label 1': NSL_KDD_OCSVM['1']},
    ]
]

ocsvm_scores = {
    'f1_score': [0.71,0.42, 0.93,0.20, 0.75,0.74],
    'precision': [0.63,0.56, 0.98,0.13, 0.65,0.88],
    'recall' : [0.81,0.34, 0.90,0.41, 0.88,0.64]
}

isolation_forest_scores = {

    'f1_score':     [0.70,0.40, 0.85,0.48, 0.83,0.85],
    'precision':   [0.62,0.54, 0.80,0.59, 0.78,0.90],
    'recall':      [0.80,0.32, 0.90,0.40, 0.88,0.81]
}

autoencoder_scores = {
    'f1_score':     [0.64,0.50, 0.85,0.46, 0.75,0.74],
    'precision':   [0.65,0.50, 0.80,0.58, 0.,65,0.88],
    'recall':      [0.64,0.51, 0.90,0.38, 0.88,0.64]
}
