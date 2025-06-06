IEEE_CIS_QSVM = {
  'Label 0': {'precision': 0.97, 'recall': 0.96, 'f1-score': 0.965, 'support': 900.0},
  'Label 1': {'precision': 0.85, 'recall': 0.88, 'f1-score': 0.865, 'support': 100.0},
  'accuracy': 0.95,
  'macro avg': {'precision': 0.91, 'recall': 0.92, 'f1-score': 0.915, 'support': 1000.0},
  'weighted avg': {'precision': 0.95, 'recall': 0.95, 'f1-score': 0.95, 'support': 1000.0}
}

IEEE_CIS_QNN = {
  'Label 0': {'precision': 0.98, 'recall': 0.96, 'f1-score': 0.97, 'support': 900.0},
  'Label 1': {'precision': 0.86, 'recall': 0.92, 'f1-score': 0.89, 'support': 100.0},
  'accuracy': 0.9649,
  'macro avg': {'precision': 0.92, 'recall': 0.94, 'f1-score': 0.93, 'support': 1000.0},
  'weighted avg': {'precision': 0.96, 'recall': 0.96, 'f1-score': 0.96, 'support': 1000.0}
}

IEEE_CIS_QAE = {
  'Label 0': {'precision': 0.87, 'recall': 0.83, 'f1-score': 0.85, 'support': 900.0},
  'Label 1': {'precision': 0.45, 'recall': 0.58, 'f1-score': 0.51, 'support': 100.0},
  'accuracy': 0.835,
  'macro avg': {'precision': 0.66, 'recall': 0.71, 'f1-score': 0.68, 'support': 1000.0},
  'weighted avg': {'precision': 0.81, 'recall': 0.835, 'f1-score': 0.82, 'support': 1000.0}
}

SECOM_QSVM = {
  'Label 0': {'precision': 0.95, 'recall': 0.94, 'f1-score': 0.945, 'support': 1557.0},
  'Label 1': {'precision': 0.75, 'recall': 0.8, 'f1-score': 0.77, 'support': 98.0},
  'accuracy': 0.84,
  'macro avg': {'precision': 0.85, 'recall': 0.87, 'f1-score': 0.86, 'support': 1655.0},
  'weighted avg': {'precision': 0.93, 'recall': 0.94, 'f1-score': 0.93, 'support': 1655.0}
}

SECOM_QNN = {
  'Label 0': {'precision': 0.96, 'recall': 0.94, 'f1-score': 0.95, 'support': 1557.0},
  'Label 1': {'precision': 0.82, 'recall': 0.87, 'f1-score': 0.84, 'support': 98.0},
  'accuracy': 0.9351,
  'macro avg': {'precision': 0.89, 'recall': 0.905, 'f1-score': 0.895, 'support': 1655.0},
  'weighted avg': {'precision': 0.93, 'recall': 0.935, 'f1-score': 0.934, 'support': 1655.0}
}

SECOM_QAE = {
  'Label 0': {'precision': 0.85, 'recall': 0.81, 'f1-score': 0.83, 'support': 1557.0},
  'Label 1': {'precision': 0.55, 'recall': 0.7, 'f1-score': 0.62, 'support': 98.0},
  'accuracy': 0.82,
  'macro avg': {'precision': 0.7, 'recall': 0.755, 'f1-score': 0.725, 'support': 1655.0},
  'weighted avg': {'precision': 0.81, 'recall': 0.82, 'f1-score': 0.815, 'support': 1655.0}
}

NSL_KDD_QSVM = {
  'Label 0': {'precision': 0.87, 'recall': 0.85, 'f1-score': 0.86, 'support': 743.0},
  'Label 1': {'precision': 0.84, 'recall': 0.86, 'f1-score': 0.85, 'support': 1250.0},
  'accuracy': 0.85,
  'macro avg': {'precision': 0.855, 'recall': 0.855, 'f1-score': 0.855, 'support': 1993.0},
  'weighted avg': {'precision': 0.85, 'recall': 0.85, 'f1-score': 0.85, 'support': 1993.0}
}

NSL_KDD_QNN = {
  'Label 0': {'precision': 0.78, 'recall': 0.73, 'f1-score': 0.755, 'support': 743.0},
  'Label 1': {'precision': 0.7, 'recall': 0.75, 'f1-score': 0.725, 'support': 1250.0},
  'accuracy': 0.7427,
  'macro avg': {'precision': 0.74, 'recall': 0.74, 'f1-score': 0.74, 'support': 1993.0},
  'weighted avg': {'precision': 0.745, 'recall': 0.743, 'f1-score': 0.744, 'support': 1993.0}
}

NSL_KDD_QAE = {
  'Label 0': {'precision': 0.82, 'recall': 0.78, 'f1-score': 0.8, 'support': 743.0},
  'Label 1': {'precision': 0.76, 'recall': 0.8, 'f1-score': 0.78, 'support': 1250.0},
  'accuracy': 0.8,
  'macro avg': {'precision': 0.79, 'recall': 0.79, 'f1-score': 0.79, 'support': 1993.0},
  'weighted avg': {'precision': 0.8, 'recall': 0.8, 'f1-score': 0.8, 'support': 1993.0}
}


quantum_models_results = [
    # IEEE_CIS classical models
    [
        {'Label 0': IEEE_CIS_QAE['Label 0'], 'Label 1': IEEE_CIS_QAE['Label 1']},
        {'Label 0': IEEE_CIS_QNN['Label 0'], 'Label 1': IEEE_CIS_QNN['Label 1']},
        {'Label 0': IEEE_CIS_QSVM['Label 0'], 'Label 1': IEEE_CIS_QSVM['Label 1']},
    ],
    # ISCOM classical models
    [
        {'Label 0': SECOM_QAE['Label 0'], 'Label 1': SECOM_QAE['Label 1']},
        {'Label 0': SECOM_QNN['Label 0'], 'Label 1': SECOM_QNN['Label 1']},
        {'Label 0': SECOM_QSVM['Label 0'], 'Label 1': SECOM_QSVM['Label 1']},
    ],
    # NSL-KDD classical models
    [
        {'Label 0': NSL_KDD_QAE['Label 0'], 'Label 1': NSL_KDD_QAE['Label 1']},
        {'Label 0': NSL_KDD_QNN['Label 0'], 'Label 1': NSL_KDD_QNN['Label 1']},
        {'Label 0': NSL_KDD_QSVM['Label 0'], 'Label 1': NSL_KDD_QSVM['Label 1']},
    ]
]


QNN_scores = {
    'f1_score': [0.95,0.84, 0.97,0.89, 0.755,0.725],
    'precision': [0.96,0.82, 0.98,0.86, 0.78,0.7],
    'recall': [0.94,0.87, 0.96,0.92, 0.73,0.75]
}

QAE_scores = {
    'f1_score': [0.755,0.725, 0.83,0.51, 0.85,0.51],
    'precision': [0.78,0.7, 0.87,0.45, 0.87,0.45],
    'recall': [0.73,0.75, 0.83,0.58, 0.83,0.58]
}

QSVM_scores = {
    'f1_score': [0.945,0.77, 0.965,0.865, 0.86,0.85],
    'precision': [0.95,0.75, 0.97,0.85, 0.87,0.84],
    'recall': [0.94,0.8, 0.96,0.88, 0.85,0.86]
}