import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = 'C:/Users/raman/OneDrive/Desktop/web_scrape/output.xlsx'  
df = pd.read_excel(excel_file_path)
df['Number of Reviews'] = pd.to_numeric(df['Number of Reviews'], errors='coerce')
reviews_by_company = df.groupby('Company')['Number of Reviews'].sum()

plt.figure(figsize=(8, 8))
plt.pie(reviews_by_company, labels=reviews_by_company.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Total Reviews by Company')
plt.show()
