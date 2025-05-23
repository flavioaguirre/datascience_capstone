# SpaceX Falcon 9 First Stage Landing Prediction 🚀

## Description

This project was part of the final phase of the IBM Data Science Professional Certification and aimed to estimate the economic feasibility of SpaceX launches by predicting the probability of a successful landing for the Falcon 9 first stage. Since reusing this stage significantly reduces the cost per launch (from $165 million to $62 million), having a reliable prediction model represents a strategic advantage for both SpaceX and its potential competitors.

The dataset was provided by IBM, and the project followed all stages of the data science lifecycle: from data acquisition through the SpaceX API, through data cleansing and transformation (ETL), to exploratory data analysis (EDA), data visualization, and predictive modeling. The project development was structured into four separate modules, each using Jupyter Notebooks to run the code and present the data. A fifth module, the final presentation, was moved directly to the root directory as "presentation."

The final model used the K-Nearest Neighbors algorithm and achieved an accuracy of 83% (despite the other models tested being slightly different). Multiple factors influencing landing success were identified, confirming that this outcome can be predicted based on measurable patterns. This approach demonstrates the true applicability of machine learning in the aerospace industry.

## Modules

1. **Data Collection**: using web scraping and the official SpaceX API.
2. **Exploratory Analysis**: using Pandas, Seaborn, matplotlib, and SQL queries.
3. **Data Visualization**: using Dash (interactive interface) and Folium (geographic maps).
4. **Predictive modeling**: Using KNN with an accuracy of 83%.
5. **Final Presentation**: PDF and PowerPoint files along with the generated images.

## How to Run

1. Clone the repository

   ```bash
   git clone https://github.com/flavioaguirre/datascience_capstone.git
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
3. We activate the virtual environment:

   On Windows:

   ```bash
   venv/Scripts/activate
   ```

   On Linux:

   ```bash
   source venv/bin/activate
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Run the notebooks or scripts in order.

## Technologies Used

- Python
- Pandas, Numpy, Scikit-Learn
- Matplotlib, Seaborn, Dash, Plotly, Folium
- SQLite
- Jupyter Notebooks

## Contact

Flavio Aguirre - [LinkedIn](https://www.linkedin.com/in/flavio-aguirre-12784a252/) - flavioaguirre0@gmail.com
