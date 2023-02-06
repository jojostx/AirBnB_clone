"""
Base model for all other models to
inherit from
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs) -> None:
        """initializes all attributes
        """
        if not kwargs:
            self.id = f'{uuid.uuid4()}'
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if (key == "updated_at" or key == "created_at"):
                    value = datetime.strptime(value, f)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """returns class name, id and attribute dictionary
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the updated_at timestamp
        """
        self.updated_at = datetime.now()
        storage.save()


    def to_dict(self):
        """creates a new dictionary, adding a key and returning
        datetimes converted to strings
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict
