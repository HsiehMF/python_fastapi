from ..schema.base import BasePokemon


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = \
                super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Pocket(metaclass=Singleton):
    def __init__(self):
        self.pocket = []
        self.count = 0
        self.filter_result = []

    def insert(self, pokemon_name: str, data: BasePokemon):
        self.count+=1
        data.number = self.count
        data.name = pokemon_name

        if(len(self.pocket) == 0):
            if(data.evolutions is not None):
                for role in data.evolutions:
                    self.count+=1
                    role.number = self.count
        else:
            for role in self.pocket:
                if(role.evolutions is not None):
                    for role in data.evolutions:
                        self.count+=1
                        role.number = self.count
        self.pocket.append(data)
        return data

    def read(self):
        return self.pocket
    
    def read_by_id(self, id: int):
        for role in self.pocket:
            if role.number == id:
                return role.dict()
            else:
                if role.evolutions is not None:
                    for evolution in role.evolutions:
                        if evolution.number == id:
                            return evolution.dict()

    def update(self, id: int, data: BasePokemon):
        for role in self.pocket:
            if role.number == id:
                role.name = data.name
                role.types = data.types
                return role
            else:
                if role.evolutions is not None:
                    for evolution in role.evolutions:
                        if evolution.number == id:
                            evolution.name = data.name
                            evolution.types = data.types
                            return evolution

    def delete(self, id:int):
        for role in self.pocket:
            if role.number == id:
                self.pocket.remove(role)
                return role
            if role.evolutions is not None:
                for evolution in role.evolutions:
                    if evolution.number == id:
                        if(len(role.evolutions) == 1):        # if delete, role.evolutions will be an empty array, we must to set it to None
                            role.evolutions.remove(evolution)
                            role.evolutions = None
                            return evolution
                        else:
                            role.evolutions.remove(evolution)
                            return evolution
    
    def filter(self, filter_type: str):
        self.filter_result = []
        for role in self.pocket:
            for type in role.types:
                if(type == filter_type):
                    self.filter_result.append(role)
        return self.filter_result
