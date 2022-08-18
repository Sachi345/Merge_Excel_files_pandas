import pandas as pd

df1 = pd.read_excel(r'output_f1.xlsx')
df2 = pd.read_excel(r'output_f2.xlsx')

print(df1.shape)
print(df2.shape)

df_combined = pd.DataFrame(df1.merge(df2, on='cust_no', how='left'))
print(df_combined.to_string())

df_combined.to_excel('merged.xlsx')
