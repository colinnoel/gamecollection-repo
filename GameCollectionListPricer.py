from IndividualGamePricerNoURL import Game
from datetime import datetime
#from GameCollection import GameCollection

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M")
game_count = 0
total_game_collection_value = float(0)


game1 = {
    'Title' : 'Pokemon Platinum',
    'Console' : 'Nintendo DS',
    'Condition' : 'cib',
    'Game Price' : 0.00
}

game2 = {
    'Title' : 'Pokemon Emerald',
    'Console' : 'Gameboy Advance',
    'Condition' : 'loose',
    'Game Price' : 0.00
}

game3 = {
    'Title' : 'Super Smash Bros. Ultimate',
    'Console' : 'Nintendo Switch',
    'Condition' : 'cib',
    'Game Price' : 0.00
}
# Our example game collection is a List, with dictionaries (games) inside
example_game_list = [game1, game2, game3]


for game in example_game_list:
    # Instantiate a gameObject from the IndividualGamePricerNoURL file, by filling in its parameters with our game{} dictionary
    gameObject = Game(game['Title'],game['Console'],game['Condition'])
    # Update the game's price value using our getGamePrice method
    game['Game Price'] = gameObject.getGamePrice()

    game_count += 1
    total_game_collection_value += game['Game Price']
    


print(f'Game List: {example_game_list}')
print("\n")
print(f'As of: {dt_string}, your {game_count} game collection has a value of: ${total_game_collection_value}')
