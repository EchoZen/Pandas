import pandas as pd, os, numpy as np
os.chdir(r'C:\Users\zchen\Documents\Shopee Python Challenge\Workshops')

# cars= {'Brand':['Honda','Toyota','Ford'],
#        'Price':[22000,25000,23000]}
# cars_df= pd.DataFrame(cars, columns=['Brand','Price'],index=['car 1','car 2','car 3'])


# # Adding columns
# year=[2010,2011,2008]
# cars_df['Year']= year
# # To control where the column is inserted
# cars_df.insert(1,'Model',['Civic','Prius','Focus'],True)  # 1 is the column index
# # True allows duplication of column names. False by default
# cars_df['Discount']= 0.1*cars_df['Price']
# cars_df['Final price']= cars_df['Price']- cars_df['Discount']
# # print(cars_df)

# # Adding rows
# new_car_1= {'Brand':'Hyundai','Model':'Avante','Price':20000} # Missing year
# # Year, discount and final price would have NaN (not a number)
# # Have to reassign when appending
# cars_df= cars_df.append(new_car_1, ignore_index=True)
# # ignore index means letting it create another row
# # However, the index reverts back to its default (0,1,2,3)
# print(cars_df)

# # Adding rows using .loc method
# # .loc[] uses square bracket
# cars_df.loc['car 4']= ['Hyundai','Avante',20000,2010,2000,18000] # Must be in order
# print(cars_df)
#
# # Modifying existing rows
# cars_df.loc['car 3']= ['Suzuki','Swift',26000, 2013, 2600, 23400]
# print(cars_df)

# importing data
pokemon_df= pd.read_csv('Pokemon_Gen_1-8.csv')
pd.set_option('display.max_rows', None) # Instead of none, if say 10, will display 10 rows
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# # One way to dispaly a few columns
# print(pokemon_df[['#','Name','Generation']]) # Must have 2 lists! List in list

# Another way to display few columns using .loc
# Since using .loc, not using number but name of row/column
# Multiple column names require additional [], list
# pokemon_generation=pokemon_df.loc[:,['#','Name','Generation']]
# print(pokemon_generation)
