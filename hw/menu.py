import os
from product_card import ProductCard
from hw.catalog_handlers import JsonParser, TxtDeserializer


class Menu:
    """
    Класс управления карточками товаров с автоматическим сохранением в JSON.
    """

    def __init__(self, json_file: str = "data.json") -> None:
        """
        Инициализация менеджера карточек.

        Args:
            json_file: Путь к JSON файлу для хранения данных
        """

        self.json_file = json_file
        self.json_parser = JsonParser()
        self.cards = {}
        self._load_cards()

    def _load_cards(self) -> None:
        """Загружает карточки из JSON файла при запуске."""

        if os.path.exists(self.json_file):
            try:
                items = self.json_parser.load_from_file(self.json_file)

                for item in items:
                    self.cards[item.get_card_id()] = item
                print(f"Загружено {len(self.cards)} карточек из {self.json_file}")
            except:
                print(f"Не удалось загрузить данные из {self.json_file}. Создан новый каталог.")
        else:
            print(f"Файл {self.json_file} не найден. Создан новый каталог. Данные будут сохраняться в {self.json_file}")

    def _save_cards(self) -> None:
        """Сохраняет все карточки в JSON файл."""

        items = list(self.cards.values())
        self.json_parser.save_to_file(items, self.json_file)

    def create_card(self, number: str, card_id: str, data: dict) -> ProductCard:
        """
        Добавление новой карточки в систему.

        Args:
            number: Порядковый номер
            card_id: Уникальный идентификатор карточки
            data: Словарь с данными для создания карточки

        Returns:
            ProductCard: Созданная и сохранённая карточка

        Raises:
            ValueError: При попытке создать карточку с существующим ID
        """

        if card_id in self.cards:
            raise ValueError(f"Карточка с ID {card_id} уже существует")

        card = ProductCard(
            number=number,
            card_id=card_id,
            name=data["name"],
            quantity=data["quantity"],
            status=data["status"],
            supplier=data["supplier"],
            manufacturer=data["manufacturer"],
            cost=data["cost"],
            location=data["location"],
            city=data["city"]
        )

        self.cards[card_id] = card
        self._save_cards()

        print(f"Карточка {card_id} сохранена в {self.json_file}")

        return card

    def get_card(self, card_id: str) -> dict:
        """
        Получение данных карточки по ID.

        Args:
            card_id: Идентификатор карточки

        Returns:
            dict: Словарь с данными карточки

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        return self.cards[card_id].get_data()

    def get_card_object(self, card_id: str) -> ProductCard:
        """
        Получение объекта карточки по ID.

        Args:
            card_id: Идентификатор карточки

        Returns:
            ProductCard: Объект карточки

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        return self.cards[card_id]

    def update_card(self, card_id: str, data: dict) -> ProductCard:
        """
        Обновление существующей карточки в системе.

        Args:
            card_id: Идентификатор обновляемой карточки
            data: Словарь с обновляемыми данными

        Returns:
            ProductCard: Обновленная карточка

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        card = self.cards[card_id]

        if "name" in data:
            card.set_name(data["name"])

        if "quantity" in data:
            card.set_quantity(data["quantity"])

        if "status" in data:
            card.set_status(data["status"])

        if "supplier" in data:
            card.set_supplier(data["supplier"])

        if "manufacturer" in data:
            card.set_manufacturer(data["manufacturer"])

        if "cost" in data:
            card.set_cost(data["cost"])

        if "location" in data:
            card.set_location(data["location"])

        if "city" in data:
            card.set_city(data["city"])

        self._save_cards()

        print(f"Карточка {card_id} обновлена и сохранена в {self.json_file}")

        return card

    def delete_card(self, card_id: str) -> None:
        """
        Удаление карточки из системы.

        Args:
            card_id: Идентификатор удаляемой карточки

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        self.cards.pop(card_id)
        self._save_cards()

        print(f"Карточка {card_id} удалена из каталога и из {self.json_file}")

    def list_cards(self) -> None:
        """
        Вывод краткой информации обо всех карточках в системе.
        """

        if not self.cards:
            print("\nНет созданных карточек")
        else:
            print("\n" + "=" * 80)

            for card in self.cards.values():
                data = card.get_data()

                print(
                    f"№: {data['№']} | ID: {data['ID']} | {data['Наименование']} | "
                    f"{data['Состояние']} | {data['Количество']} шт. | {data['Стоимость']}"
                )

            print(f"\nВсего карточек: {len(self.cards)}")

    def import_from_txt(self, txt_file: str) -> int:
        """
        Импортирует карточки из TXT файла, заменяя текущий каталог.
        """

        if not os.path.exists(txt_file):
            print(f"Файл {txt_file} не найден")
            return 0

        txt_deserializer = TxtDeserializer()
        imported_items = txt_deserializer.load_from_file(txt_file)

        self.cards.clear()

        for item in imported_items:
            self.cards[item.get_card_id()] = item

        self._save_cards()

        print(f"Импортировано {len(imported_items)} карточек из {txt_file} (старые карточки удалены)")

        return len(imported_items)