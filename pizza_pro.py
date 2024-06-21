import pandas as pd
from matplotlib import pyplot as plt

df= pd.read_csv('pizza_sales_2015.csv')

# Unique values
distinct_values= df.nunique()
#print(distinct_values)

# Unique values per column
unique_values= df.apply(lambda col: col.unique())
#print(unique_values)

# Number if cells per column
count_cells= df.count()
#print(count_cells)


# Data type
#print(df.dtypes)


# Discriptive data
statistical_data= df.describe()
#print(statistical_data)

# Frequency per data
frq= {col: df[col].value_counts for col in df.select_dtypes(include= ['object', 'category']).columns}
#print(frq)


table= df.filter(['id', 'date', 'time', 'name', 'size', 'type', 'price'])


# Splitting the id column and take only the id part I want 
table[['year', 'ID']]= table['id'].str.split('-', expand= True)
table['ID']

# Check for duplicates

duplicates= table.duplicated().sum() #There are 954 duplicates
#print(table[table.duplicated(keep= False)])


# Remove duplicates
non_duplicated_table= table.drop_duplicates(subset= 'id', keep= 'first')
#print(non_duplicated_table.head(20)) to check if 0017 is not repeated 
#print(non_duplicated_table.nunique())

# Check if there are empty values
non_duplicated_table.isnull().sum()

cleaned_table= non_duplicated_table

# get a month column
cleaned_table['date'] = pd.to_datetime(cleaned_table['date'])
cleaned_table['month'] = cleaned_table['date'].dt.month

sales_table= cleaned_table.filter(['size', 'type', 'price'])
total_sales= sales_table.value_counts().reset_index()
total_sales.columns= ['size', 'type', 'price', 'sales/type']

# High sales
#print("Highest sales:")
#print(total_sales.head(10))

# Low sales
#print("Lowest Sales:")
#print(total_sales.tail(10))

# total_sales sorted by type of pizza
#print("Total sales:")
#print(total_sales.sort_values('type'))


total_sales['profit']= total_sales['price'] * total_sales['sales/type']

# High profit
#print(total_sales.sort_values(by= 'profit', ascending= False))

# Plotting
plt.bar(x= total_sales['type'], height= total_sales['profit'], width= 0.5, align= 'center')
#plt.show()