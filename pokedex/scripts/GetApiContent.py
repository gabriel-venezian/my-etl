import requests
import json


class GetApiContent:
  """
  Class responsible for get pokémon information from PokeAPI.
  """
  def poke_data_list(POKE_API_URL: str):
    """
    Method to get information about the first pokémon generation.

    Args:
      POKE_API_URL (str): API's url.
    
    Returns:
      List: pokémon data (id, name, image and primitive type).
    """
    # Create poke_data_list starting empty
    poke_data_list = []
    # Iterate information about the first pokémon generation
    for poke_index in range(1, 152):
      # Connect to the API
      poke_api = requests.get(f'{POKE_API_URL}/{poke_index}')
      # Parse API data with JSON
      poke_information = json.loads(poke_api.text)
      # pokémon information
      poke_id = poke_index
      poke_name = poke_information['name']
      poke_image = poke_information['sprites']['other']['official-artwork']['front_default']
      poke_type = poke_information['types'][0]['type']['name']
      # Create a list of tuples with pokémon information
      poke_information = (poke_id, poke_name, poke_image, poke_type)
      poke_data_list.append(poke_information)
    return poke_data_list
