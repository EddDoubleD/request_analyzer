from sys import argv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

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
    data = pd.read_csv(directory + '/result.csv')
    # Подготовка данных
    X = data[['count']]  # Предиктор (независимая переменная)
    y = data['failed'].astype('int')  # Целевая переменная

    # Разделение данных на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Создание модели логистической регрессии
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Предсказание на тестовой выборке
    y_pred = model.predict(X_test)
    # Матрица ошибок (confusion matrix)
    conf_matrix = confusion_matrix(y_test, y_pred)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap=plt.cm.Blues)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()

    # Отчёт о классификации
    print(classification_report(y_test, y_pred))

    # Вероятности принадлежности классам
    y_prob = model.predict_proba(X_test)[:, 1]
    plt.scatter(X_test, y_prob, color='red')
    plt.xlabel('Number of Parameters', fontsize=12)
    plt.ylabel('Probability of Failure', fontsize=12)
    plt.title('Probability of Request Failure Vs Number of Parameters')
    plt.grid(True)
    plt.show()
