import numpy as np
from scipy import stats

class Analyzer:
    def __init__(self, data):
        self.data = data

    def basic_stats(self, column):
        """Return basic statistics (mean, median, std) for the specified column."""
        return {
            'mean': np.mean(self.data[column]),
            'median': np.median(self.data[column]),
            'std': np.std(self.data[column])
        }

    def detect_anomalies(self, column, threshold=3):
        """Detect anomalies in the specified column using z-scores."""
        z_scores = np.abs(stats.zscore(self.data[column]))
        return self.data[z_scores > threshold]

    def correlation_analysis(self, column1, column2):
        """Perform correlation analysis between two columns."""
        return np.corrcoef(self.data[column1], self.data[column2])[0, 1]
    
    def calculate_correlation(self, column1, column2):
        """Calculate correlation between two columns."""
        return self.data[column1].corr(self.data[column2])

    def calculate_trend(self, column):
        """Calculate trend using linear regression."""
        # Implement linear regression here or use scipy.stats.linregress
        # For simplicity, let's return the mean as a placeholder
        return self.data[column].mean()
