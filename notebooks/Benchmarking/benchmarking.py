import numpy as np
from scipy.stats import wilcoxon
import matplotlib.pyplot as plt
from results_classical import *
from results_quantum import *

class ModelComparisonPipeline:
    def __init__(self, alpha=0.1):
        self.alpha = alpha

    def format_model_scores(self, classification_reports):
        f1s, precisions, recalls = [], [], [],
        for report  in classification_reports:
            f1s.extend([report['Label 0']['f1-score'], report['Label 1']['f1-score']])
            precisions.extend([report['Label 0']['precision'], report['Label 1']['precision']])
            recalls.extend([report['Label 0']['recall'], report['Label 1']['recall']])


        return {
            'f1_score': f1s,
            'precision': precisions,
            'recall': recalls,
        }

    def average_scores_across_models(self, model_scores_list):
        avg_scores = {}
        for key in model_scores_list[0]:
            all_values = np.array([model[key] for model in model_scores_list])
            avg_scores[key] = list(np.mean(all_values, axis=0))
        return avg_scores

    def compare_models_on_all_metrics(self, scores_model_a, scores_model_b, model_a_name, model_b_name):
        print(f"\nComparing '{model_a_name}' vs '{model_b_name}' using Wilcoxon Signed-Rank Test across metrics:\n")

        for metric in scores_model_a:
            try:
                print(f"{'='*150}")
                a_scores = np.array(scores_model_a[metric], dtype=float)
                b_scores = np.array(scores_model_b[metric], dtype=float)
                if len(a_scores) != len(b_scores):
                    print(f"Skipping metric '{metric}': Unequal lengths.")
                    continue
                stat, p_value = wilcoxon(a_scores, b_scores, alternative='greater', method='auto')
                print(f"Metric: {metric}")
                print(f" - {model_a_name} scores: {a_scores}")
                print(f" - {model_b_name} scores: {b_scores}")
                print(f" - Test Statistic: {stat:.4f}")
                print(f" - p-value: {p_value:.4f}")
                if p_value < self.alpha:
                    print(f"Result: '{model_a_name}' performs significantly better than '{model_b_name}' (p < {self.alpha}) → Reject H₀")
                else:
                    print(f"Result: No significant difference between '{model_a_name}' and '{model_b_name}' (p ≥ {self.alpha}) → Fail to reject H₀")
            except Exception as e:
                print(f"Error with metric '{metric}': {e}\n")

    def compare_classical_vs_quantum(self, classical_models_results, quantum_models_results, model_a_name, model_b_name):
        classical_formatted, quantum_formatted = [], []

        for reports in classical_models_results:
            classical_formatted.append(self.format_model_scores(reports))
        for reports in quantum_models_results:
            quantum_formatted.append(self.format_model_scores(reports))

        avg_classical = self.average_scores_across_models(classical_formatted)
        avg_quantum = self.average_scores_across_models(quantum_formatted)


        # Compare metrics statistically
        self.compare_models_on_all_metrics(avg_quantum, avg_classical, "Quantum Models (avg)", "Classical Models (avg)")



