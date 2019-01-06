from collections import UserDict, defaultdict

class AbstractWidgetsCollection(UserDict):
    def __init__(self, pair):
        self.data = defaultdict(list, pair)
