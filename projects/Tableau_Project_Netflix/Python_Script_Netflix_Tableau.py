import pandas as pd

# clean id
df = pd.read_csv('netflix_titles.csv')

df['show_id'] = df['show_id'].str.replace('s', '')

# clean rating and duration
for i in df.index:
    if df.loc[i, 'rating'] in ['74 min', '84 min', '66 min']:
        df.loc[i, 'duration'] = df.loc[i, 'rating']
        df.loc[i, 'rating'] = None

# table categories
cat = df[['show_id', 'listed_in']]

cat['listed_in'] = cat['listed_in'].str.split(', ')

cat = cat.explode('listed_in')

cat.to_csv('netflix_categories.csv')

# table countries
countries = df[['show_id', 'country']]

countries['country'] = countries['country'].str.split(', ')

countries = countries.explode('country')

countries.to_csv('netflix_countries.csv')

# table directors
directors = df[['show_id', 'director']]

directors['director'] = directors['director'].str.split(', ')

directors = directors.explode('director')

directors.to_csv('netflix_directors.csv')

# table cast
cast = df[['show_id', 'cast']]

cast['cast'] = cast['cast'].str.split(', ')

cast = cast.explode('cast')

cast.to_csv('netflix_cast.csv')

# clean table netflix_titles

df = df.drop(columns=['listed_in', 'country', 'director', 'cast', 'description'])

df.to_csv('clean_netflix_titles.csv', index=False)



