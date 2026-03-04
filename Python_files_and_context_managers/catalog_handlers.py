import json
import csv
from abc import ABC, abstractmethod
from typing import Dict, List, Any

from product_card import ProductCard
from product_catalog import ProductCatalog


class IItemCatalogSerializer(ABC):
    """Интерфейс для сериализации каталога товаров"""

    @abstractmethod
    def serialize(self, catalog: ProductCatalog) -> Dict[str, List[Dict[str, Any]]]:
        pass


class IItemCatalogDeserializer(ABC):
    """Интерфейс для десериализации каталога товаров"""

    @abstractmethod
    def deserialize(self, file_path: str) -> ProductCatalog:
        pass


class JsonCatalogHandler(IItemCatalogSerializer, IItemCatalogDeserializer):
    """
    Объединенный класс для сериализации и десериализации каталога товаров в JSON.
    """

    def __init__(self, encoding: str = 'utf-8'):
        self._encoding = encoding

    def serialize(self, catalog: ProductCatalog) -> Dict[str, List[Dict[str, Any]]]:
        items = []

        for item in catalog.get_items():
            # Преобразуем статус в числовое значение для JSON
            state_map = {
                "Новое": 2,
                "Новый остаток": 2,
                "состоит на учёте": 2,
                "черновик": 1,
                "списано": 3
            }
            state_value = state_map.get(item.get_status(), 2)

            items.append({
                'number': item.get_number(),
                'product_id': item.get_card_id(),
                'name': item.get_name(),
                'quantity': item.get_quantity(),
                'state': state_value,
                'supplier': item.get_supplier(),
                'manufacturer': item.get_manufacturer(),
                'price': item.get_cost(),
                'location': item.get_location(),
                'city': item.get_city()
            })

        return {'items': items}

    def deserialize(self, file_path: str) -> ProductCatalog:
        with open(file_path, 'r', encoding=self._encoding) as file:
            data = json.load(file)

        items = []

        for item_data in data['items']:
            state_map = {
                1: "черновик",
                2: "состоит на учёте",
                3: "списано"
            }
            status_value = state_map.get(item_data.get('state', 2), "состоит на учёте")

            item = ProductCard(
                number=item_data.get('number', ''),
                card_id=item_data.get('product_id', ''),
                name=item_data.get('name', ''),
                quantity=item_data.get('quantity', 0),
                status=status_value,
                supplier=item_data.get('supplier', ''),
                manufacturer=item_data.get('manufacturer', ''),
                cost=float(item_data.get('price', 0)),
                location=item_data.get('location', ''),
                city=item_data.get('city', '')
            )
            items.append(item)

        return ProductCatalog(items)

    def save_to_file(self, catalog: ProductCatalog, file_path: str) -> None:
        data = self.serialize(catalog)
        with open(file_path, 'w', encoding=self._encoding) as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Каталог сохранен в {file_path}")

    def load_from_file(self, file_path: str) -> ProductCatalog:
        catalog = self.deserialize(file_path)
        print(f"Каталог загружен из {file_path}")
        return catalog


class CsvCatalogHandler(IItemCatalogDeserializer):
    """
    Класс для десериализации каталога товаров из CSV файла.
    Формат файла: разделитель ';', первая строка - заголовки
    Поля: №;ID;Наименование;Количество;Состояние;Поставщик;Производитель;Стоимость;Местоположение;Город
    """

    def __init__(self, encoding: str = 'utf-8', delimiter: str = ';'):
        self._encoding = encoding
        self._delimiter = delimiter

    def deserialize(self, file_path: str) -> ProductCatalog:
        items = []

        with open(file_path, 'r', encoding=self._encoding) as file:
            reader = csv.DictReader(file, delimiter=self._delimiter)

            for row in reader:
                item = self._create_item_from_row(row)
                items.append(item)

        return ProductCatalog(items)

    def _create_item_from_row(self, row: dict) -> ProductCard:
        # Очищаем стоимость от "руб." и преобразуем в число
        cost_str = row.get('Стоимость', '0').replace('руб.', '').strip()
        try:
            cost = float(cost_str)
        except ValueError:
            cost = 0.0

        # Создаем карточку товара со всеми полями из CSV
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

        return item

    def load_from_file(self, file_path: str) -> ProductCatalog:
        catalog = self.deserialize(file_path)
        print(f"Каталог загружен из {file_path}")
        return catalog