import json
import csv
from abc import ABC, abstractmethod
from typing import Dict, List, Any

from product_card import ProductCard


class BaseSerializer(ABC):
    """
    Интерфейс для сериализации каталога товаров.
    """

    @abstractmethod
    def serialize(self, items: List[ProductCard]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Сериализует список товаров в словарь.

        Args:
            items: Список карточек товаров

        Returns:
            dict: Словарь с данными каталога
        """

        pass


class BaseDeserializer(ABC):
    """
    Интерфейс для десериализации каталога товаров.
    """

    @abstractmethod
    def deserialize(self, filename: str) -> List[ProductCard]:
        """
        Десериализует список товаров из файла.

        Args:
            filename: Путь к файлу для десериализации

        Returns:
            list: Список карточек товаров
        """

        pass


class JsonParser(BaseSerializer, BaseDeserializer):
    """
    Класс для сериализации и десериализации списка товаров в JSON.
    """

    def serialize(self, items: List[ProductCard]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Сериализует список товаров в формат JSON.

        Args:
            items: Список карточек товаров

        Returns:
            dict: Словарь с данными каталога
        """

        items_data = []

        for item in items:
            items_data.append(item.to_dict())

        return {'items': items_data}

    def deserialize(self, filename: str) -> List[ProductCard]:
        """
        Десериализует список товаров из файла JSON.

        Args:
            filename: Путь к файлу JSON

        Returns:
            list: Список карточек товаров
        """

        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        items = []

        for item_data in data['items']:
            item = ProductCard.from_dict(item_data)
            items.append(item)

        return items

    def save_to_file(self, items: List[ProductCard], filename: str) -> None:
        """
        Сохраняет список товаров в JSON файл.

        Args:
            items: Список карточек товаров
            filename: Путь для сохранения файла
        """

        data = self.serialize(items)

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print(f"Список товаров сохранен в {filename}")

    def load_from_file(self, filename: str) -> List[ProductCard]:
        """
        Загружает список товаров из JSON файла.

        Args:
            filename: Путь к JSON файлу

        Returns:
            list: Список карточек товаров
        """

        items = self.deserialize(filename)

        print(f"Список товаров загружен из {filename}")

        return items


class TxtDeserializer(BaseDeserializer):
    """
    Класс для десериализации списка товаров из TXT файла.
    Ожидаемые поля: №;ID;Наименование;Количество;Состояние;Поставщик;Производитель;Стоимость;Местоположение;Город
    """

    def deserialize(self, filename: str) -> List[ProductCard]:
        """
        Десериализует список товаров из TXT файла.

        Args:
            filename: Путь к TXT файлу

        Returns:
            list: Список карточек товаров
        """

        items = []

        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')

            for row in reader:
                cost_str = row.get('Стоимость', '0').replace('руб.', '').strip()
                try:
                    cost = float(cost_str)
                except ValueError:
                    cost = 0.0

                item = ProductCard(
                    number=row.get('№', ''),
                    card_id=row.get('ID', ''),
                    name=row.get('Наименование', ''),
                    quantity=int(row.get('Количество', 0)),
                    status=row.get('Состояние', ''),
                    supplier=row.get('Поставщик', ''),
                    manufacturer=row.get('Производитель', ''),
                    cost=cost,
                    location=row.get('Местоположение', ''),
                    city=row.get('Город', '')
                )
                items.append(item)

        return items

    def load_from_file(self, filename: str) -> List[ProductCard]:
        """
        Загружает список товаров из TXT файла.

        Args:
            filename: Путь к TXT файлу

        Returns:
            list: Список карточек товаров
        """

        items = self.deserialize(filename)

        print(f"Список товаров загружен из {filename}")

        return items