
import csv
from Archive.IndividualGamePricer import Game


def main():
    
    collection = GameCollection(r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 1" + ".csv", r'C:\\Users\\cn\\OneDrive\\Desktop\\Python Projects\\game collection project\\' + "Game Collection Example 2" + ".csv")
    GameCollection.show_number_of_games

if __name__ == "__main__":
    main()


class GameCollection:
    number_of_games = 0
    total_value = 0

    def __init__(self,read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path


    @classmethod
    def show_number_of_games(cls):
        print(cls.number_of_games)

    @classmethod
    def show_total_value(cls):
        print(cls.total_value)



