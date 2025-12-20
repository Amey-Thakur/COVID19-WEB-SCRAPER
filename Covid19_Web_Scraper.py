# -----------------------------------------------------------------------------------------
# Project: Covid19 Web Scraper
# GitHub: https://github.com/Amey-Thakur/COVID19-WEB-SCRAPER
# Created by: Amey Thakur & Hasan Rizvi
# Batch: 2022 @ Terna Engineering College
# -----------------------------------------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests 
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# --- Setup ---
# Official Ministry of Health and Family Welfare website for live COVID-19 statistics
url = 'https://www.mohfw.gov.in/' 

# --- Extraction ---
# Make a GET request to fetch the raw HTML content from the MOHFW website
web_content = requests.get(url).content

# Parse the HTML content using BeautifulSoup's HTML parser
soup = BeautifulSoup(web_content, "html.parser")

# Lambda function to remove newlines and extra spaces from table row content
extract_contents = lambda row: [x.text.replace('\n', '') for x in row] 

stats = [] # Initialize list to store scraped data
all_rows = soup.find_all('tr') # Find all table rows in the HTML

# Iterate through each row and extract individual cell data
for row in all_rows: 
    stat = extract_contents(row.find_all('td')) # Extract all data cells (td) within the row
    # The requirement is a list of exactly length 5 (Sr.No, States, Confirmed, Recovered, Deceased)
    if len(stat) == 5: 
        stats.append(stat)

# --- Data Processing ---
# Convert the scraped list of lists into a structured Pandas DataFrame
new_cols = ["Sr.No", "States/UT", "Confirmed", "Recovered", "Deceased"]
state_data = pd.DataFrame(data=stats, columns=new_cols)

# Convert string-based numerical data into Integers for mathematical processing
state_data['Confirmed'] = state_data['Confirmed'].map(int)
state_data['Recovered'] = state_data['Recovered'].map(int)
state_data['Deceased']  = state_data['Deceased'].map(int)

# --- Tabular Representation ---
# Displaying the processed data in a clean, professional table format using PrettyTable
table = PrettyTable()
table.field_names = new_cols
for i in stats:
    table.add_row(i)

# Append a final row for the National Totals
table.add_row(["", "Total", 
               sum(state_data['Confirmed']), 
               sum(state_data['Recovered']), 
               sum(state_data['Deceased'])])
print(table)

# --- Visualization: Bar Plot ---
# Horizontal bar plot showing Total Confirmed cases across different States/UTs
sns.set_style("ticks")
plt.figure(figsize=(15, 10))
plt.barh(state_data["States/UT"], state_data["Confirmed"],
         align='center', color='lightblue', edgecolor='blue')

# Formatting the plot axes and labels
plt.xlabel('No. of Confirmed cases', fontsize=18)
plt.ylabel('States/UT', fontsize=18)
plt.gca().invert_yaxis()   # Maintain original order by inverting the Y-axis
plt.xticks(fontsize=14) 
plt.yticks(fontsize=14)
plt.title('Total Confirmed Cases Statewise', fontsize=20)

# Display value labels on each bar for better readability
for index, value in enumerate(state_data["Confirmed"]):
    plt.text(value, index, str(value), fontsize=12, verticalalignment='center')
plt.show()  

# --- Visualization: Donut Chart ---
# Nationwide distribution of stats (Confirmed, Recovered, Deceased) using a Donut Chart
group_size = [sum(state_data['Confirmed']), 
               sum(state_data['Recovered']), 
               sum(state_data['Deceased'])]

group_labels = ['Confirmed\n' + str(sum(state_data['Confirmed'])), 
                'Recovered\n' + str(sum(state_data['Recovered'])), 
                'Deceased\n'  + str(sum(state_data['Deceased']))]
custom_colors = ['skyblue', 'yellowgreen', 'tomato']

plt.figure(figsize=(5, 5))
plt.pie(group_size, labels=group_labels, colors=custom_colors)

# Creating the central white circle to transform the Pie Chart into a Donut Chart
central_circle = plt.Circle((0, 0), 0.5, color='white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)

# Final styling and title for the Nationwide chart
plt.rc('font', size=12) 
plt.title('Nationwide Stats: Confirmed, Recovered and Deceased Cases', fontsize=16)
plt.show()