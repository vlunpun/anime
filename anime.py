import requests
import json
import pandas as pd
import sqlalchemy as db

#Function to get anime information by ID using Jikan API v4
def get_anime_info(id):
  url = f"https://api.jikan.moe/v4/anime/{id}"
  response = requests.get(url)

  if response.status_code == 200:
    #Convert to dictionary
    anime_data = response.json()
    return anime_data
  else:
    return None
  
# Main function to test the API and load data into database
def main():
  # ID for the anime "Naruto"
  anime_id = 20
  # Fetch anime information
  anime_info = get_anime_info(anime_id)

  if anime_info:
    anime = anime_info['data']
    print(f"Title: {anime['title']}")
    print(f"Episodes: {anime['episodes']}")
    print(f"Synopsis: {anime['synopsis']}")
  else:
    print("Failed to fetch anime information.")

  #Convert dictionary to DataFrame
  anime_dict = {
    'title': [anime['title']],
    'episodes': [anime['episodes']],
    'synopsis': [anime['synopsis']]
  }

  anime_df = pd.DataFrame.from_dict(anime_dict)
        
  #Create a SQLite database engine
  engine = db.create_engine('sqlite:///anime_database.db')
        
  #Write the DataFrame to the SQLite database
  anime_df.to_sql('anime_info', con=engine, if_exists='replace', index=False)
        
  #Query the database and print the results
  with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM anime_info;")).fetchall()
    print(pd.DataFrame(query_result))

#Run function
if __name__ == "__main__":
  main()

