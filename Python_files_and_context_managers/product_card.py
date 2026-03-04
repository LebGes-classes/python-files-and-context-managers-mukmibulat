import datetime
from typing import Dict, Any, Optional


class ProductCard:
    """
    Класс для создания, изменения, просматривания и списания карточки.
    """

    STATUS_DRAFT = "черновик"
    STATUS_IN_STOCK = "состоит на учёте"
    STATUS_WRITTEN_OFF = "списано"

    def __init__(
            self,
            number: str,  # №
            card_id: str,  # ID
            name: str,  # Наименование
            quantity: int,  # Количество
            status: str,  # Состояние
            supplier: str,  # Поставщик
            manufacturer: str,  # Производитель
            cost: float,  # Стоимость
            location: str,  # Местоположение
            city: str  # Город
    ) -> None:
        self._number = number
        self._card_id = card_id
        self._name = name
        self._quantity = quantity
        self._status = status
        self._supplier = supplier
        self._manufacturer = manufacturer
        self._cost = cost
        self._location = location
        self._city = city

    def get_number(self) -> str:
        return self._number

    def get_card_id(self) -> str:
        return self._card_id

    def get_name(self) -> str:
        return self._name

    def get_quantity(self) -> int:
        return self._quantity

    def get_status(self) -> str:
        return self._status

    def get_supplier(self) -> str:
        return self._supplier

    def get_manufacturer(self) -> str:
        return self._manufacturer

    def get_cost(self) -> float:
        return self._cost

    def get_location(self) -> str:
        return self._location

    def get_city(self) -> str:
        return self._city

    def set_name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Название не может быть пустым")
        self._name = value.strip()

    def set_quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._quantity = value

    def set_status(self, value: str) -> None:
        self._status = value

    def set_supplier(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Поставщик не может быть пустым")
        self._supplier = value.strip()

    def set_manufacturer(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Производитель не может быть пустым")
        self._manufacturer = value.strip()

    def set_cost(self, value: float) -> None:
        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self._cost = value

    def set_location(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Местоположение не может быть пустым")
        self._location = value.strip()

    def set_city(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Город не может быть пустым")
        self._city = value.strip()

    def get_data(self) -> dict:
        return {
            "№": self._number,
            "ID": self._card_id,
            "Наименование": self._name,
            "Количество": self._quantity,
            "Состояние": self._status,
            "Поставщик": self._supplier,
            "Производитель": self._manufacturer,
            "Стоимость": f"{self._cost:.2f} руб.",
            "Местоположение": self._location,
            "Город": self._city
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            'number': self._number,
            'card_id': self._card_id,
            'name': self._name,
            'quantity': self._quantity,
            'status': self._status,
            'supplier': self._supplier,
            'manufacturer': self._manufacturer,
            'cost': self._cost,
            'location': self._location,
            'city': self._city
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ProductCard':
        return cls(
            number=data['number'],
            card_id=data['card_id'],
            name=data['name'],
            quantity=data['quantity'],
            status=data['status'],
            supplier=data['supplier'],
            manufacturer=data['manufacturer'],
            cost=data['cost'],
            location=data['location'],
            city=data['city']
        )