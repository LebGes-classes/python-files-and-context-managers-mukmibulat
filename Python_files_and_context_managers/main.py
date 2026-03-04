from catalog_handlers import CsvCatalogHandler, JsonCatalogHandler

# Читаем из CSV
csv_handler = CsvCatalogHandler()
catalog = csv_handler.load_from_file("data.txt")

# Сохраняем в JSON
json_handler = JsonCatalogHandler()
json_handler.save_to_file(catalog, "data.json")

print("Конвертация завершена!")