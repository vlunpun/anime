import requests
import json

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
  
# Main function to test the API
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

#Run function
if __name__ == "__main__":
  main()