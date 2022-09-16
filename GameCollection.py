class GameCollection:
    game_collection_value = float(0)

    def __init__(self, game_collection_list):
        self.game_collection_list = game_collection_list
        
    def __iter__(self):
        return self
    
    def showGameCount(self):
        print(len(self.game_collection_list))

    @classmethod
    def showGameCollectionValue(cls):
        print(cls.game_collection_value)


