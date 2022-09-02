from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    """
    subclass of product
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    """
    subclass of product
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


class Creator(ABC):
    """
    The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        TODO: implementation of the factory method
        """

    def some_operation(self) -> str:
        """
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    """
    subclass of creator
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    """
    subclass of creator
    """
    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    print(f"Client: {creator.some_operation()}")


if __name__ == "__main__":
    print("App: Launched with the Concreator1")
    client_code(ConcreteCreator1())
    print("\n")
    print("App: Launched with the Concreator2")
    client_code(ConcreteCreator2())
