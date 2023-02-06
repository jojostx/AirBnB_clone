"""
Base model for all other models to
inherit from
"""
import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self) -> None:
        """initializes all attributes
        """
        self.id = f'{uuid.uuid4()}'
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the updated_at timestamp
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datetimes converted to strings
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict
