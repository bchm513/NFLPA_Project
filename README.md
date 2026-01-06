Appendix A: Software and Libraries

All analyses were conducted in Python using widely adopted, open-source scientific computing and machine learning libraries. The following packages were used to support data processing, modeling, evaluation, and visualization.

Data Processing and Numerical Computation

pandas
Utilized for structured data ingestion, cleaning, transformation, and aggregation.

numpy
Used for numerical operations, array manipulation, and handling of missing values.

Data Visualization

matplotlib
Employed for generating static figures, including model diagnostics and feature importance visualizations.

seaborn
Used to enhance visual clarity and presentation of statistical plots.

Machine Learning Framework

scikit-learn (sklearn)
Served as the primary machine learning framework for preprocessing, modeling, and evaluation:

Data splitting via train_test_split

Feature scaling using StandardScaler

Categorical encoding with LabelEncoder

Missing data handling through SimpleImputer

Injury risk classification using RandomForestClassifier

Post-injury performance prediction using RandomForestRegressor

Player risk profiling via KMeans clustering

Model workflow management using Pipeline

Dimensionality reduction using PCA

Visualization of decision trees via plot_tree

Gradient Boosting Models

XGBoost (xgboost)
Applied for injury risk classification to capture nonlinear relationships and complex feature interactions. XGBoost was selected due to its strong empirical performance on structured tabular data.

Model Evaluation Metrics

classification_report
Used to assess classification performance via precision, recall, and F1-score.

mean_squared_error (MSE) and mean_absolute_error (MAE)
Used to evaluate regression model accuracy.

R² score
Used to assess explanatory power of regression models.

Exploratory and Multivariate Analysis

pandas.plotting.parallel_coordinates
Used for visual comparison of multivariate player profiles across clustering results.

Computational Environment

Python version: 3.13 or higher

All modeling procedures assume numeric feature inputs following preprocessing

Missing data were explicitly handled prior to scaling and model estimation

Warnings generated during execution were suppressed using the Python warnings module to improve interpretability of outputs.