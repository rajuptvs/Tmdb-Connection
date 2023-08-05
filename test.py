from themoviedb import TMDb
import pandas as pd
tmdb = TMDb(key="eb980dd63dfdf03b72a4c9189ec414b0")
movies = tmdb.search().tv("T")
print(movies)
# convert the result above into dataframe
df = pd.DataFrame(movies)
# print(df)



# convert the result above into dataframe
# df = pd.DataFrame(j)
