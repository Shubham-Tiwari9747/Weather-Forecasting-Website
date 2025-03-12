import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weatherAUS.csv')

# Display the first 5 rows of the DataFrame
print(df.head(5))

# Display column names
print(df.columns)

# Replace 'No' with 0 and 'Yes' with 1 in 'RainToday' and 'RainTomorrow' columns
df['RainToday'].replace({'No': 0, 'Yes': 1}, inplace=True)
df['RainTomorrow'].replace({'No': 0, 'Yes': 1}, inplace=True)

def possible_rain():
    # Plotting RainTomorrow Indicator
    fig = plt.figure(figsize=(8, 5))
    df.RainTomorrow.value_counts(normalize=True).plot(kind='bar', color=['skyblue', 'navy'], alpha=0.9, rot=0)
    plt.title('RainTomorrow Indicator No(0) and Yes(1) in the Imbalanced Dataset')
    plt.show()

def datatype():
    # Plotting data types distribution
    fig, axarr = plt.subplots(1, 2, figsize=(20, 8))

    # Pie chart for data types distribution
    df.dtypes.value_counts().plot.pie(explode=[0.1, 0.1], autopct='%1.1f%%', shadow=True, ax=axarr[1])
    axarr[1].set_title("Type of our data ", fontsize=18)

    # Bar chart for data types distribution
    df.dtypes.value_counts().plot(kind='bar', ax=axarr[0])
    plt.title('Type of our data')
    axarr[0].set_title("Type of our data ", fontsize=18)

    plt.show()

def analyze():
    # Analyzing Average monthly rainfall in India
    data = pd.read_csv("Weather Data in India from 1901 to 2017.csv")

    # Plotting Average monthly rainfall
    ax = data[['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']].mean().plot.bar(
        width=0.5, linewidth=2, figsize=(16, 10)
    )
    
    plt.xlabel('Month', fontsize=30)
    plt.ylabel('Monthly Rainfall (in mm)', fontsize=30)
    plt.title('Monthly Rainfall in Subdivisions of India', fontsize=25)
    ax.tick_params(labelsize=10)
    plt.grid()
    plt.show()

# Uncomment and call the functions if needed
# possible_rain()
# datatype()
# analyze()
