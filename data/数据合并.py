import pandas as pd

file_paths = [
    r"C:\Users\Hydrolox\OneDrive\桌面\data\data1.csv",
    r"C:\Users\Hydrolox\OneDrive\桌面\data\data2.csv",
    r"C:\Users\Hydrolox\OneDrive\桌面\data\data3.csv",
    r"C:\Users\Hydrolox\OneDrive\桌面\data\data4.csv"
]

encodings = ['utf-8', 'utf-8-sig', 'gbk', 'latin1']

dataframes = []

for fp in file_paths:
    for encoding in encodings:
        try:
            df = pd.read_csv(fp, encoding=encoding)
            dataframes.append(df)
            break 
        except UnicodeDecodeError:
            continue 

if dataframes:
    combined_data = pd.concat(dataframes, ignore_index=True)
    print(combined_data)

combined_data.to_csv( r"C:\Users\Hydrolox\OneDrive\桌面\data\datacombined_data.csv", index=False)