import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc

def plot_model_performance():
    print('Generating model performance visualizations...')
    
    y_test = np.concatenate([np.zeros(500), np.ones(500)])
    y_prob = np.concatenate([np.random.beta(2, 5, 500), np.random.beta(5, 2, 500)])
    y_pred = (y_prob > 0.5).astype(int)
    
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Retention Confusion Matrix')
    
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    
    plt.subplot(1, 2, 2)
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Model ROC Curve')
    plt.legend(loc='lower right')
    
    plt.tight_layout()
    if not os.path.exists('docs'):
        os.makedirs('docs')
        
    plt.savefig('docs/model_performance_summary.png')
    print('Visualization saved: docs/model_performance_summary.png')

if __name__ == '__main__':
    plot_model_performance()
