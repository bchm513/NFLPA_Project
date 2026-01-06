## Appendix A: Software and Libraries

All analyses were conducted in Python using widely adopted, open-source scientific computing and machine learning libraries. The following packages were used to support data processing, modeling, evaluation, and visualization.

### Data Processing and Numerical Computation
- **pandas**  
  Used for structured data ingestion, cleaning, transformation, and aggregation.
- **numpy**  
  Used for numerical operations, array manipulation, and handling of missing values.

### Data Visualization
- **matplotlib**  
  Employed for generating static figures, including model diagnostics and feature importance visualizations.
- **seaborn**  
  Used to enhance visual clarity and presentation of statistical plots.

### Machine Learning Framework
- **scikit-learn (sklearn)**  
  Served as the primary machine learning framework for preprocessing, modeling, and evaluation:
  - Data splitting via `train_test_split`
  - Feature scaling using `StandardScaler`
  - Categorical encoding with `LabelEncoder`
  - Missing data handling through `SimpleImputer`
  - Injury risk classification using `RandomForestClassifier`
  - Post-injury performance prediction using `RandomForestRegressor`
  - Player risk profiling via `KMeans` clustering
  - Model workflow management using `Pipeline`
  - Dimensionality reduction using `PCA`
  - Decision tree visualization via `plot_tree`

### Gradient Boosting Models
- **XGBoost (xgboost)**  
  Applied for injury risk classification to capture nonlinear relationships and complex feature interactions. XGBoost was selected due to its strong empirical performance on structured tabular data.

### Model Evaluation Metrics
- **classification_report**  
  Used to assess classification performance via precision, recall, and F1-score.
- **mean_squared_error (MSE)** and **mean_absolute_error (MAE)**  
  Used to evaluate regression model accuracy.
- **R² score**  
  Used to assess explanatory power of regression models.

### Exploratory and Multivariate Analysis
- **pandas.plotting.parallel_coordinates**  
  Used for visual comparison of multivariate player profiles across clustering results.

### Computational Environment
- Python version: **3.9 or higher**
- All modeling procedures assume numeric feature inputs following preprocessing
- Missing data were explicitly handled prior to scaling and model estimation

Warnings generated during execution were suppressed using the Python `warnings` module to improve interpretability of outputs.

## Appendix B: Details about the Project

This project is a submission for the 2025 NFLPA data competition. Group members include Benjamin Harris-Myers and Sarah Akiki, and our team name is "The Cloudscrapers". We are representing the Trojans Sports Research Lab's Graduate Student team. 

### Executive Summary 

The National Football League Collective Bargaining Agreement (CBA), while an extensive piece of legislation, contains little detailed provisions regarding the connections between travel, game environment, and their impact on player health, injury risk, or post-injury workload. To be clear, the CBA only discusses team travel within the context of it being a reimbursable expense, an omission that seems increasingly untenable considering the league’s growing travel demands and wide variation in environmental conditions across venues.

Using publicly available data from Pro Football Reference and NFL.com’s injury report, this study examines the relationship between travel burden, environmental factors, prior injury history, and subsequent player workload during the 2016–2025 seasons, corresponding to the playing era of the NFL as determined by our group. We construct a cumulative workload metric combining snap counts and various on-field production stats following documented injuries, and model this outcome as a function of travel distance, time-zone changes, altitude, climate, and player production stats. Our central hypothesis is that more difficult travel conditions and dramatic environmental transitions are positively correlated with elevated injury risk and increased cumulative workload following injury, reflecting heightened physiological stress and incomplete recovery. While our hypothesis was not entirely proven, our findings do suggest a relationship between environmental stressors and injury rate and post-injury performance. 

By empirically linking travel and environmental variability to post-injury workload outcomes, this study identifies travel as a structural blind spot in the current CBA and provides evidence relevant to future negotiations concerning player health, workload and roster management.

### Results

Most notably, cumulative workload, proxied by snap count, emerged as the strongest and most consistent predictor of injury risk across both Random Forest and XGBoost models. This reinforces evidence that sustained on-field exposure, as opposed to isolated conditions as our hypothesis suggests, is the primary driver of injury risk. From a policy perspective, this supports advocating for expanded roster sizes and greater player rotation, enabling teams to distribute snaps more evenly and reduce overuse-related injuries. Additionally, elevation change consistently ranked among the most important non-workload predictors in both modeling and clustering analyses. This suggests that abrupt altitude shifts introduce physiological stress that is not currently addressed by the CBA. Given established medical research on acclimatization, the NFLPA could reasonably push for additional rest, medical accommodations, or roster flexibility when teams face significant elevation changes.

### How to Run

All data scraping and feature engineering occurs in the data_prep folder. Run all for each notebook in the order of 
1. game_level_scraper.ipynb
2. injury_scraper.ipynb
3. player_stat_scraper.ipynb
4. feature_engineering.ipynb
5. combine_csvs.ipynb

All modeling and analysis occurs in the data_modeling folder. You will need to organize your data in the format below to align with the code. Data has not been provided to the Github. Run all for each notebook in the order of
1. modeling_setup.ipynb
2. initial_analysis.ipynb
3. modeling.ipynb