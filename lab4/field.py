goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

def field(items, *args):
    assert len(args) > 0

    for item in items:
        if len(args) == 1:
            key = args[0]
            if key in item and item[key] is not None:
                yield item[key]
        else:
            result = {}
            has_value = False  # Флаг для проверки, есть ли хотя бы одно непустое поле
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_value = True
            if has_value:
                yield result


if __name__ == "__main__":
    for item in field(goods, 'title'):
        print(item, end = " ")
    print()
    for item in field(goods, 'title', 'price'):
        print(item)