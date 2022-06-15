import pandas as pd
df = pd.read_csv("data_data.csv")
# datafile.dropna([3])
df.drop('locationid', axis=1, inplace=True) 


### MANUAL CURATING
# find rows in `df1` which contain search_word
search_word = input(str("What Keyword would you like to search by? -> "))
result = (df[df['title'].str.contains(search_word)])
formatted_result = result[~result['customprinturl'].isnull()]
print(formatted_result)

### PRINT TESTING
# print(result)
# print(len(formatted_result))
# print(formatted_result)
# formatted_result = result.dropna(subset=27, axis=0)

# In [30]: df.dropna(subset=[1])
# print(result['title'])


### CATAGORISED CURATING

# for word in df['title']:
    # print(len(word))


# pd.options.display.max_rows = 1000
# print(pd.options.display.max_rows)
# print(df.info())
# print(datafile)


# https://raw.githubusercontent.com/NationalGalleryOfArt/opendata/main/data/objects.csv