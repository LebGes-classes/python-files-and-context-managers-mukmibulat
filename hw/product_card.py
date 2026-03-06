from typing import Dict, Any


class ProductCard:
    """
    Класс для создания и управления карточкой товара.
    """

    def __init__(
            self,
            number: str,
            card_id: str,
            name: str,
            quantity: int,
            status: str,
            supplier: str,
            manufacturer: str,
            cost: float,
            location: str,
            city: str
    ) -> None:
        """
        Конструктор карточки товара.

        Args:
            number: Порядковый номер
            card_id: ID карточки
            name: Наименование товара
            quantity: Количество единиц товара
            status: Состояние товара
            supplier: Наименование поставщика
            manufacturer: Наименование производителя
            cost: Стоимость единицы товара в рублях
            location: Место хранения на складе
            city: Город
        """

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
        """Возвращает порядковый номер."""

        return self._number

    def get_card_id(self) -> str:
        """Возвращает ID карточки."""

        return self._card_id

    def get_name(self) -> str:
        """Возвращает наименование товара."""

        return self._name

    def get_quantity(self) -> int:
        """Возвращает количество единиц товара."""

        return self._quantity

    def get_status(self) -> str:
        """Возвращает состояние товара."""

        return self._status

    def get_supplier(self) -> str:
        """Возвращает наименование поставщика."""

        return self._supplier

    def get_manufacturer(self) -> str:
        """Возвращает наименование производителя."""

        return self._manufacturer

    def get_cost(self) -> float:
        """Возвращает стоимость единицы товара."""

        return self._cost

    def get_location(self) -> str:
        """Возвращает место хранения на складе."""

        return self._location

    def get_city(self) -> str:
        """Возвращает город."""

        return self._city

    def set_name(self, value: str) -> None:
        """
        Изменение наименования товара.

        Args:
            value: Новое наименование товара

        Raises:
            ValueError: При попытке установить пустое наименование
        """

        if not value or not value.strip():
            raise ValueError("Название не может быть пустым")
        self._name = value.strip()

    def set_quantity(self, value: int) -> None:
        """
        Изменение количества товара.

        Args:
            value: Новое количество единиц товара

        Raises:
            ValueError: При попытке установить отрицательное количество
        """

        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._quantity = value

    def set_status(self, value: str) -> None:
        """
        Изменение состояния товара.

        Args:
            value: Новое состояние
        """

        self._status = value

    def set_supplier(self, value: str) -> None:
        """
        Изменение поставщика товара.

        Args:
            value: Новое наименование поставщика

        Raises:
            ValueError: При попытке установить пустого поставщика
        """

        if not value or not value.strip():
            raise ValueError("Поставщик не может быть пустым")
        self._supplier = value.strip()

    def set_manufacturer(self, value: str) -> None:
        """
        Изменение производителя товара.

        Args:
            value: Новое наименование производителя

        Raises:
            ValueError: При попытке установить пустого производителя
        """

        if not value or not value.strip():
            raise ValueError("Производитель не может быть пустым")
        self._manufacturer = value.strip()

    def set_cost(self, value: float) -> None:
        """
        Изменение стоимости товара.

        Args:
            value: Новая стоимость в рублях

        Raises:
            ValueError: При попытке установить отрицательную стоимость
        """

        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self._cost = value

    def set_location(self, value: str) -> None:
        """
        Изменение местоположения товара.

        Args:
            value: Новое место хранения

        Raises:
            ValueError: При попытке установить пустое местоположение
        """

        if not value or not value.strip():
            raise ValueError("Местоположение не может быть пустым")
        self._location = value.strip()

    def set_city(self, value: str) -> None:
        """
        Изменение города.

        Args:
            value: Новый город

        Raises:
            ValueError: При попытке установить пустой город
        """

        if not value or not value.strip():
            raise ValueError("Город не может быть пустым")
        self._city = value.strip()

    def get_data(self) -> dict:
        """
        Полные данные карточки в формате словаря.

        Returns:
            dict: Словарь со всеми полями карточки
        """

        return {
            "№": self._number,
            "ID": self._card_id,
            "Наименование": self._name,
            "Количество": self._quantity,
            "Состояние": self._status,
            "Поставщик": self._supplier,
            "Производитель": self._manufacturer,
            "Стоимость": f"{self._cost} руб.",
            "Местоположение": self._location,
            "Город": self._city
        }

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразует объект в словарь для сериализации.

        Returns:
            dict: Словарь с данными карточки
        """

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
        """
        Создает объект из словаря после десериализации.

        Args:
            data: Словарь с данными карточки

        Returns:
            ProductCard: Объект карточки товара
        """

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