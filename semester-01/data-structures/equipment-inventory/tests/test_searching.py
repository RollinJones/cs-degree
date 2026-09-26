from equipment_inventory.searching import search_by_id, search_by_type

def test_search_by_id():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500},
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000}
    ]

    result = search_by_id(inventory, 102)

    assert result["name"] == "Gas Blower"
    assert result["cost"] == 12000


def test_search_by_id_missing():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500}
    ]

    result = search_by_id(inventory, 999)

    assert result is None


def test_search_by_id_empty_inventory():
    inventory = []

    result = search_by_id(inventory, 101)

    assert result is None

def test_search_by_type():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500},
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000},
        {"id": 103, "name": "Pressure Transmitter", "type": "Sensor", "cost": 850}
    ]

    result = search_by_type(inventory, "Sensor")

    assert len(result) == 2
    assert result[0]["id"] == 101
    assert result[1]["id"] == 103


def test_search_by_type_missing():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500}
    ]

    result = search_by_type(inventory, "Pump")

    assert result == []


def test_search_by_type_empty_inventory():
    inventory = []

    result = search_by_type(inventory, "Sensor")

    assert result == []