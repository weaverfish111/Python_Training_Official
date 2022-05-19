import pandas as pd
datafile = pd.read_csv("data_data.csv")
datafile.dropna([3], inplace = True)


# pd.options.display.max_rows = 1000
# print(pd.options.display.max_rows)
print(datafile.info())

print(datafile)


# https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data/objects.csv