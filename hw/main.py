from hw.menu import Menu


def main() -> None:
    """
    Класс для запуска консольного интерфейса для работы с данными карточки.
    """

    system = Menu()

    while True:
        print("\n1 - Создать карточку")
        print("2 - Изменить карточку")
        print("3 - Просмотреть карточку")
        print("4 - Удалить карточку")
        print("5 - Список всех карточек")
        print("6 - Импорт из TXT")
        print("7 - Выход")

        choice = input("Выберите действие (1-7): ").strip()

        match choice:
            case "1":
                number = input("№: ").strip()
                card_id = input("ID карточки: ").strip()

                if not card_id:
                    print("ID не может быть пустым")
                    continue

                try:
                    name = input("Наименование: ").strip()

                    if not name:
                        print("Наименование не может быть пустым")
                        continue

                    try:
                        quantity = int(input("Количество: ").strip())
                    except ValueError:
                        print("Количество должно быть числом")
                        continue

                    status = input("Состояние: ").strip()

                    supplier = input("Поставщик: ").strip()

                    if not supplier:
                        print("Поставщик не может быть пустым")
                        continue

                    manufacturer = input("Производитель: ").strip()

                    if not manufacturer:
                        print("Производитель не может быть пустым")
                        continue

                    try:
                        cost = float(input("Стоимость: ").strip())
                    except ValueError:
                        print("Стоимость должна быть числом")
                        continue

                    location = input("Местоположение: ").strip()

                    if not location:
                        print("Местоположение не может быть пустым")
                        continue

                    city = input("Город: ").strip()

                    if not city:
                        print("Город не может быть пустым")
                        continue

                    data = {
                        "name": name,
                        "quantity": quantity,
                        "status": status,
                        "supplier": supplier,
                        "manufacturer": manufacturer,
                        "cost": cost,
                        "location": location,
                        "city": city
                    }

                    system.create_card(number, card_id, data)

                except ValueError as e:
                    print(f"Ошибка ввода данных: {e}")
                except Exception as e:
                    print(f"Ошибка при создании карточки: {e}")

            case "2":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    card = system.get_card_object(card_id)
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    continue

                data = {}
                print("(Оставьте поле пустым, если не хотите менять)")

                name = input(f"Новое наименование ({card.get_name()}): ").strip()

                if name:
                    data["name"] = name

                quantity = input(f"Новое количество ({card.get_quantity()}): ").strip()

                if quantity:
                    try:
                        data["quantity"] = int(quantity)
                    except ValueError:
                        print("Количество должно быть числом")
                        continue

                status = input(f"Новое состояние ({card.get_status()}): ").strip()

                if status:
                    data["status"] = status

                supplier = input(f"Новый поставщик ({card.get_supplier()}): ").strip()

                if supplier:
                    data["supplier"] = supplier

                manufacturer = input(f"Новый производитель ({card.get_manufacturer()}): ").strip()

                if manufacturer:
                    data["manufacturer"] = manufacturer

                cost = input(f"Новая стоимость ({card.get_cost()}): ").strip()

                if cost:
                    try:
                        data["cost"] = float(cost)
                    except ValueError:
                        print("Стоимость должна быть числом")
                        continue

                location = input(f"Новое местоположение ({card.get_location()}): ").strip()

                if location:
                    data["location"] = location

                city = input(f"Новый город ({card.get_city()}): ").strip()

                if city:
                    data["city"] = city

                if data:
                    try:
                        system.update_card(card_id, data)
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                    except Exception as e:
                        print(f"Ошибка при обновлении карточки: {e}")
                else:
                    print("Нет данных для обновления")

            case "3":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    data = system.get_card(card_id)
                    print("\n" + "-" * 40)
                    for key, value in data.items():
                        print(f"{key}: {value}")
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "4":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    card = system.get_card_object(card_id)
                    confirm = input(f"Удалить карточку '{card.get_name()}'? (да/нет): ").strip().lower()

                    if confirm == "да":
                        system.delete_card(card_id)
                    else:
                        print("Удаление отменено")

                except ValueError as e:
                    print(f"Ошибка: {e}")
                except Exception as e:
                    print(f"Ошибка при удалении карточки: {e}")

            case "5":
                system.list_cards()

            case "6":
                txt_file = input("Введите путь к TXT файлу: ").strip()

                if txt_file:
                    system.import_from_txt(txt_file)
                else:
                    print("Путь к файлу не указан")

            case "7":
                print("До свидания!")
                break

            case _:
                print("Неверный выбор. Пожалуйста, выберите 1-7")


if __name__ == "__main__":
    main()