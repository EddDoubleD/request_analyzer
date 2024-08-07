from sys import argv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


if __name__ == '__main__':
    """
    Analyzing and visualizing data to determine the linear dependence between the number of parameters in a 
    request (count) and the execution time (time). Initially, data from the CSV file is loaded into a DataFrame. 
    Then, data analysis is conducted using Pearson correlation methods and linear regression to quantify and assess 
    the potential linear relationship between variables. During the analysis, a scatter plot is created, and a trend 
    line is added for clarity of the presumed dependency. The outcomes of the analysis, including the correlation 
    coefficient, R-squared value, and P-value, help conclude the degree and significance of the relationship between 
    the number of parameters and execution time
    """
    directory = argv[1]
    # upload data
    df = pd.read_csv(directory + '/result.csv')
    print(df.head())

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='count', y='time', data=df, hue='failed')
    plt.title('Scatter plot of Cloud IDs Count vs Time')
    plt.xlabel('Number of Parameters (cloud_ids_cnt)')
    plt.ylabel('Execution Time (ms)')
    plt.show()

    # Calculating the correlation coefficient
    correlation = df['count'].corr(df['time'])
    print(f"Correlation coefficient: {correlation}")

    # Building a trend line
    slope, intercept, r_value, p_value, std_err = linregress(df['count'], df['time'])
    print(f"Slope: {slope}")
    print(f"Intercept: {intercept}")
    print(f"R-squared: {r_value ** 2}")
    print(f"P-value: {p_value}")

    # Построение линии тренда
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='count', y='time', data=df)
    plt.plot(df['count'], intercept + slope * df['count'], 'r', label='fitted line')
    plt.title('Trend Line with Scatter Points')
    plt.xlabel('Number of Parameters (count)')
    plt.ylabel('Execution Time (ms)')
    plt.legend()
    plt.show()
