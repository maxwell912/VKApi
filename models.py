from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class User:
    id: int
    first_name: str
    last_name: str
    online: int

    def __str__(self):
        return "id: {}; fisrt name: {}; last name: {}; online: {}".format(self.id,
                                                                          self.first_name,
                                                                          self.last_name,
                                                                          self.online)


@dataclass_json
@dataclass
class Album:
    id: int
    title: str
    size: int

    def __str__(self):
        return "id: {}; title: {}; size: {}".format(self.id,
                                                    self.title,
                                                    self.size)
