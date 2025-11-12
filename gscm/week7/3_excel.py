# install pandas en openpyxl
# ????

# C://python312.exe -m pip insall pandas
# C://python312.exe -m pip insall openpyxl

import pandas as pd

rows = [
    [1, "T-rex", "Super hungry"],
    [2, "Conny", "Not hungry"],
    [3, "Clyde", "Super hungry"],
]

headers = ["id", "name", "hungry status"]

df = pd.DataFrame(rows, columns=headers)

df.to_excel("./goats.xlsx", index=False)
print(df)