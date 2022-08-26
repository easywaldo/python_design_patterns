from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    product a
    """
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class AbstractProductB(ABC):
    """
    product b
    """
    @abstractmethod
    def drive(self):
        pass
    @abstractmethod
    def useful_function_b(self) -> str:
        pass
    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        pass


class CarFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class KoreaProductA(AbstractProductA):
    """
    Product A in Korea
    """
    def drive(self):
        print('dirve a mode in Korea')
        print(self.useful_function_a())
    def useful_function_a(self) -> str:
        return "feature useful mode in Korea"

class KoreaProductB(AbstractProductB):
    """
    Product B in Korea
    """
    def drive(self):
        print('dirve b mode in Korea')
        print(self.useful_function_b())
    def useful_function_b(self) -> str:
        return "feature useful mode in Korea"
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        collaborator.useful_function_a()
        print('another useful feature...')


class KoreaCarFactory(CarFactory):
    """
    Car Factory in Korea
    """
    def create_product_a(self) -> AbstractProductA:
        print('korea product a is completed')
        return KoreaProductA()
    def create_product_b(self) -> AbstractProductB:
        print('korea product b is completed')
        return KoreaProductB()
    

class UsaProductA(AbstractProductA):
    """
    Product A in USA
    """
    def drive(self):
        print('drive a mode in USA')
        print(self.useful_function_a())
    def useful_function_a(self) -> str:
        return "feature useful mode in USA"
    
class UsaProductB(AbstractProductB):
    """
    Product B in USA
    """
    def drive(self):
        print('drive b mode in USA')
        print(self.useful_function_b())
    def useful_function_b(self) -> str:
        return "feature useful mode in USA"
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        collaborator.useful_function_a()
        print('another useful feature...')

class UsaCarFactory(CarFactory):
    """
    Car Factory in USA
    """
    def create_product_a(self) -> AbstractProductA:
        print('usa product a is completed')
        return UsaProductA()
    def create_product_b(self) -> AbstractProductB:
        print('usa product b is completed')
        return UsaProductB()
    
    

k_factory = KoreaCarFactory()
u_factory = UsaCarFactory()

product_a_in_korea = k_factory.create_product_a()
product_b_in_korea = k_factory.create_product_b()

product_a_in_usa = u_factory.create_product_a()
product_b_in_usa = u_factory.create_product_b()


product_a_in_korea.drive()
product_a_in_usa.drive()

product_b_in_korea.drive()
product_b_in_usa.drive()
