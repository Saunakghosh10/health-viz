# test_script.py

import pandas as pd
from healthviz.analysis import Analyzer

# Sample data for testing
data = pd.DataFrame({
    'age': [25, 30, 35, 40, 200],  # Note: 200 is an anomaly
    'weight': [55, 70, 80, 90, 100]
})

# Initialize Analyzer
analyzer = Analyzer(data)

# Testing basic statistics
stats = analyzer.basic_stats('age')
print('Basic Statistics for Age:', stats)

# Testing anomaly detection using IQR
anomalies = analyzer.detect_anomalies_iqr('age')
print('Detected Anomalies in Age (IQR method):', anomalies)

# Testing correlation analysis
correlation = analyzer.correlation_analysis('age', 'weight')
print('Correlation between Age and Weight:', correlation)

# Testing trend calculation
trend = analyzer.calculate_trend('age')
print('Trend for Age:', trend)
