class Manufacturer:
    """Производитель"""
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

class Detail:
    """Деталь"""
    def __init__(self, id, name, man_id):
        self.id = id
        self.name = name
        self.man_id = man_id

class ManufacturerDetail:
    """Реализуем связь многие ко многим"""
    def __init__(self, man_id, det_id):
        self.man_id = man_id
        self.det_id = det_id