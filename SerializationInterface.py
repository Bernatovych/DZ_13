from abc import abstractmethod, ABC
import json, pickle


class SerializationInterface(ABC):

    @abstractmethod
    def serializer(self, data, file_name):
        pass

    @abstractmethod
    def deserializer(self, file_name):
        pass


class Json(SerializationInterface):

    def serializer(self, data, file_name):
        with open(file_name, "w") as file:
            json.dump(data, file)

    def deserializer(self, file_name):
        with open(file_name, "r") as file:
            return json.load(file)


class Bin(SerializationInterface):

    def serializer(self, data, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(data, file)

    def deserializer(self, file_name):
        with open(file_name, 'rb') as file:
            return pickle.load(file)