import sys
sys.path.insert(0, 'pokedex/scripts')
from pokedex.scripts.Constants import Constants
from pokedex.scripts.CsvExport import CsvExport
from pokedex.scripts.Database import Database
from pokedex.scripts.GetApiContent import GetApiContent
from pokedex.scripts.GraphicalInterface import GraphicalInterface


# Instantiate Database class
database = Database()
# Create database
database.create_database()
# Store pokémon information in the database 
database.store_in_database()

# Create CSV from API 
CsvExport.csv_export('poke_data_api.csv', GetApiContent.poke_data_list(Constants.POKE_API_URL()))
# Create CSV from database
CsvExport.csv_export('poke_data_database.csv', database.database_content('SELECT * FROM pokedex'))

# Start GUI
GraphicalInterface.start_gui()
