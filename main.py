# Import required libraries
import pandas as pd
import nannyml as nml
nml.disable_usage_logging()

reference = pd.read_csv("reference.csv")
analysis = pd.read_csv("analysis.csv")
 # Get the estimated performance using CBPE algorithm
cbpe = nml.CBPE(
    timestamp_column_name="timestamp",
    y_true="is_fraud",
    y_pred="predicted_fraud",
    y_pred_proba="predicted_fraud_proba",
    problem_type="classification_binary",
    metrics=["accuracy"],
    chunk_period="m"
)

cbpe.fit(reference)
est_results = cbpe.estimate(analysis)

# Calculate the realized performance
calculator = nml.PerformanceCalculator(
    y_true="is_fraud",
    y_pred="predicted_fraud",
    y_pred_proba="predicted_fraud_proba",
    timestamp_column_name="timestamp",
    metrics=["accuracy"],
    chunk_period="m",
    problem_type="classification_binary",
)
calculator = calculator.fit(reference)
calc_results = calculator.calculate(analysis)

# Compare the results and find the months with alerts
est_results.compare(calc_results).plot().show()
months_with_performance_alerts = ["april_2019", "may_2019", "june_2019"]
print(months_with_performance_alerts) 

features = ["time_since_login_min", "transaction_amount",
            "transaction_type", "is_first_transaction", 
            "user_tenure_months"]

# Calculate the univariate drift results
udc = nml.UnivariateDriftCalculator(
    timestamp_column_name="timestamp",
    column_names=features,
    chunk_period="m",
    continuous_methods=["kolmogorov_smirnov"],
    categorical_methods=["chi2"]
)

udc.fit(reference)
udc_results = udc.calculate(analysis)

# Use the correlation ranker
ranker = nml.CorrelationRanker()
ranker.fit(
    calc_results.filter(period="reference"))

correlation_ranked_features = ranker.rank(udc_results, calc_results)

# Find the highest correlating feature
display(correlation_ranked_features)
highest_correlation_feature = "time_since_login_min"
print(highest_correlation_feature)

calc = nml.SummaryStatsAvgCalculator(
    column_names=["transaction_amount"],
    chunk_period="m",
    timestamp_column_name="timestamp",
)

calc.fit(reference)
stats_avg_results = calc.calculate(analysis)

# Find the month
stats_avg_results.plot().show()
alert_avg_transaction_amount = 3069.8184
print(alert_avg_transaction_amount)
