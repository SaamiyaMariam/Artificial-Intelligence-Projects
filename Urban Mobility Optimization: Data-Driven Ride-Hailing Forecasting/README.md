# Urban Mobility Optimization: Data-Driven Ride-Hailing Forecasting

This Python script, `main.py`, is part of our AI project focused on optimizing urban mobility. It merges, processes, and analyzes various datasets related to ride-hailing services. The main steps include:

1. **Data Reading & Sorting:**
   - Reads and organizes cluster, order, POI, and weather data.
   - Sorts order data based on start region hash.

2. **Data Merging:**
   - Merges order data with cluster data.
   - Incorporates POI data into the merged dataset.

3. **Weather Data Integration:**
   - Sorts and merges weather data with the existing dataset.

4. **Rolling Sum Calculation:**
   - Calculates a rolling sum of accepted orders within a specified time window.

5. **Model Training:**
   - Utilizes machine learning models (Linear Regression) for predictive analysis.
   - Visualizes the relationship between time, order count, and other features.

Note: Paths to input files are hardcoded, and the script assumes a specific dataset structure. Ensure dataset availability and adjust paths accordingly.

**Authors:**
- Saamiya Mariam
- Bisma Haroon

**Usage:**
1. Place the script in the project repository.
2. Run the script to preprocess data and train the model.

