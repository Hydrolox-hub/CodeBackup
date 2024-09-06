import pandas as pd

file_path = 'C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\datacombined_data.csv'
df = pd.read_csv(file_path)

def contains_whitespace(row):
    return row.str.contains(r'\s+', na=False).any()

def Market_size (df):
    df2 = df[(df['partnerDesc'] != 'World') & (df['partnerDesc'] != 'China')]
    return df2.groupby('period')['primaryValue'].sum()
       

def top_10_partners(df):
    df2 = df[(df['partnerDesc'] != 'World') & (df['partnerDesc'] != 'China')]
    years = [2019, 2020, 2021, 2022, 2023]
    results = {}
    for year in years:
        df_year = df2[df2['period'] == year]
        top_10 = df_year.groupby('partnerDesc')['primaryValue'].sum().nlargest(10)
        results[year] = top_10
    result_df = pd.DataFrame(results).fillna(0)
    return result_df

def top_10_goods(df):
    df['cmdCodePrefix'] = df['cmdCode'].astype(str).str[:2]
    df2 = df[(df['partnerDesc'] != 'World') & (df['partnerDesc'] != 'China')]
    years = [2019, 2020, 2021, 2022, 2023]
    results = {}
    for year in years:
        df_year = df2[df2['period'] == year]
        top_10 = df_year.groupby('cmdCodePrefix')['primaryValue'].sum().nlargest(10)
        results[year] = top_10
    result_df = pd.DataFrame(results).fillna(0)
    return result_df


df = df[~df.apply(contains_whitespace, axis=1)]
df.drop_duplicates(inplace=True)
print("去重后的数据行数:", len(df))
df_import = df[df['flowDesc'] == 'Import']
df_export = df[df['flowDesc'] == 'Export']
print("Import数据行数:", len(df_import))
print("Export数据行数:", len(df_export))
df_import.to_csv('C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\import_data.csv', index=False)
df_export.to_csv('C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\export_data.csv', index=False)

#进口数据
import_data = pd.read_csv('C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\import_data.csv')
print("Import World Market Size:", Market_size(import_data))
print("Import Top 10 Partners:", top_10_partners(import_data))
print("Import Top 10 Goods:", top_10_goods(import_data))

#出口数据
export_data = pd.read_csv('C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\export_data.csv')
print("Export World Market Size:", Market_size(export_data))
print("Export Top 10 Partners:", top_10_partners(export_data))
print("Export Top 10 Goods:", top_10_goods(export_data))

#将所有输出写入文件
with open('C:\\Users\\Hydrolox\\OneDrive\\桌面\\data\\output.txt', 'w') as f:
    f.write("Import World Market Size:\n")
    f.write(str(Market_size(import_data)))
    f.write("\nImport Top 10 Partners:\n")
    f.write(str(top_10_partners(import_data)))
    f.write("\nImport Top 10 Goods:\n")
    f.write(str(top_10_goods(import_data)))
    f.write("\nExport World Market Size:\n")
    f.write(str(Market_size(export_data)))
    f.write("\nExport Top 10 Partners:\n")
    f.write(str(top_10_partners(export_data)))
    f.write("\nExport Top 10 Goods:\n")
    f.write(str(top_10_goods(export_data)))
    f.close()
    print("输出已写入文件")
