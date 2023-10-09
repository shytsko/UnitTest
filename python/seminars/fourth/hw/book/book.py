import dataclasses


@dataclasses.dataclass
class Book:
    pk: str
    title: str
    author: str
