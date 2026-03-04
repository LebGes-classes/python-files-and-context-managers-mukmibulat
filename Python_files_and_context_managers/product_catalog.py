from typing import List, Optional
from product_card import ProductCard


class ProductCatalog:
    """Класс для управления каталогом товаров"""

    def __init__(self, items: List[ProductCard] = None):
        self._items = items or []

    def get_items(self) -> List[ProductCard]:
        return self._items

    def add_item(self, item: ProductCard) -> None:
        self._items.append(item)

    def remove_item(self, card_id: str) -> None:
        self._items = [item for item in self._items if item.get_card_id() != card_id]

    def find_item(self, card_id: str) -> Optional[ProductCard]:
        for item in self._items:
            if item.get_card_id() == card_id:
                return item
        return None

    def get_items_count(self) -> int:
        return len(self._items)