import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = 'C:/Users/paulu/OneDrive/Desktop/Masterarbeit/data/breast_cancer_age20_40.csv'

# CSV-Datei einlesen
df = pd.read_csv(file_path, sep=';')

# Erste Zeilen anzeigen
print("Erste 5 Zeilen:")
print(df.head())

