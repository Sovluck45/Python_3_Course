import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = \
        {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date
        }
    with open("orders.json", "r", encoding="utf-8") as json_read:
        orders_file = json.loads(json_read.read())
    orders_file["orders"].append(dict_to_json)

    with open("orders.json", "w", encoding="utf-8") as json_dict:
        json.dump(orders_file, json_dict, indent=4, ensure_ascii=False)


write_order_to_json("Printer", 1, 3000, "Иванов", "21.05.20")
write_order_to_json("Computer", 1, 100000, "Петров", "12.09.21")
write_order_to_json("TV", 1, 40000, "Сидоров", "05.07.22")
