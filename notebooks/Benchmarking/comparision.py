from benchmarking import *
from results_classical import *
from results_quantum import *

pipeline = ModelComparisonPipeline(alpha=0.1)

#Isolation forest vs OCSVM
pipeline.compare_models_on_all_metrics(isolation_forest_scores,ocsvm_scores,"Isolation Forest", "OCSVM")

#QNN vs OCSVM
pipeline.compare_models_on_all_metrics(QNN_scores,ocsvm_scores,"QNN", "OCSVM")

#QNN vs QAE
pipeline.compare_models_on_all_metrics(QNN_scores,QAE_scores,"QNN", "QAE")

#QNN vs Isolation Forest
pipeline.compare_models_on_all_metrics(QNN_scores,isolation_forest_scores,"QNN", "Isolation Forest")

#QNN vs QSVM
pipeline.compare_models_on_all_metrics(QNN_scores,QSVM_scores,"QNN", "QSVM")

#QNN vs AE
pipeline.compare_models_on_all_metrics(QNN_scores,autoencoder_scores,"QNN", "AE")

#QSVM vs Isolation Forest
pipeline.compare_models_on_all_metrics(QSVM_scores,isolation_forest_scores,"QSVM", "Isolation Forest")

#QSVM vs AE
pipeline.compare_models_on_all_metrics(QSVM_scores,autoencoder_scores,"QSVM", "AE")

#QSVM vs QAE
pipeline.compare_models_on_all_metrics(QSVM_scores,QAE_scores,"QSVM", "QAE")

#QSVM vs OCSVM
pipeline.compare_models_on_all_metrics(QSVM_scores,ocsvm_scores,"QSVM", "OCSVM")

#QSVM vs QNN
pipeline.compare_models_on_all_metrics(QSVM_scores,QNN_scores,"QSVM", "QNN")

#QAE vs AE
pipeline.compare_models_on_all_metrics(QAE_scores,autoencoder_scores,"QAE", "AE")

#QAE vs Isolation Forest
pipeline.compare_models_on_all_metrics(QAE_scores,isolation_forest_scores,"QAE", "Isolation Forest")

#Average quantum scores vs average classical scores
pipeline.compare_classical_vs_quantum(classical_models_results, quantum_models_results, "Classical", "Quantum")