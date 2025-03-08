#📌 Introduction:

This project focuses on detecting financial fraud using NannyML, an advanced monitoring tool for tracking model performance and data drift. The analysis involves estimating model performance, detecting drift in key features, and identifying correlations that could indicate fraudulent activity.

📊 Performance Estimation using CBPE

The Confidence-Based Performance Estimation (CBPE) method is used to estimate model accuracy over time. The process involves:

1️⃣ Loading reference and analysis datasets.
2️⃣ Fitting CBPE on the reference dataset.
3️⃣ Estimating model performance for the analysis dataset.
4️⃣ Comparing estimated vs. realized performance to detect performance degradation.


🚨 Performance Alerts Found in:

April 2019
May 2019
June 2019


🔎 Univariate Drift Detection

To detect data drift in individual features, we use statistical tests:
Kolmogorov-Smirnov Test (for continuous features).
Chi-Square Test (for categorical features).


Key features analyzed:

✔ time_since_login_min
✔ transaction_amount
✔ transaction_type
✔ is_first_transaction
✔ user_tenure_months


📈 Feature Importance & Correlation
A Correlation Ranker is applied to identify features most correlated with performance degradation. The highest correlating feature detected was:

🔹 time_since_login_min
💰 Average Transaction Amount Monitoring
Using a Summary Statistics Calculator, we monitor the average transaction amount over time. A significant alert was found with an average transaction amount of $3069.8184.


#🚀 Conclusion

This project highlights the importance of continuous monitoring in fraud detection. By using NannyML, we can:

✅ Detect performance degradation.
✅ Identify features contributing to fraud detection issues.
✅ Monitor data drift and take proactive measures.


