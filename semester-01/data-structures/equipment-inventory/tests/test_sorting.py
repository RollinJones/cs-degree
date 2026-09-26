from equipment_inventory.sorting import sort_by_cost

def test_sort_by_cost():

    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500},
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000},
        {"id": 103, "name": "Pressure Transmitter", "type": "Sensor", "cost": 850}
    ]

    result = sort_by_cost(inventory)

    assert result[0]["cost"] == 850
    assert result[1]["cost"] == 4500
    assert result[2]["cost"] == 12000

def test_sort_empty_inventory():
    inventory = []

    result = sort_by_cost(inventory)

    assert result == []

def test_sort_already_sorted():
    inventory = [
        {"id": 101, "name": "A", "type": "Sensor", "cost": 100},
        {"id": 102, "name": "B", "type": "Sensor", "cost": 200},
        {"id": 103, "name": "C", "type": "Sensor", "cost": 300}
    ]

    result = sort_by_cost(inventory)

    assert [equipment["cost"] for equipment in result] == [100, 200, 300]

def test_sort_reverse_sorted():
    inventory = [
        {"id": 101, "name": "A", "type": "Sensor", "cost": 300},
        {"id": 102, "name": "B", "type": "Sensor", "cost": 200},
        {"id": 103, "name": "C", "type": "Sensor", "cost": 100}
    ]

    result = sort_by_cost(inventory)

    assert [equipment["cost"] for equipment in result] == [100, 200, 300]

def test_sort_duplicate_costs():
    inventory = [
        {"id": 101, "name": "A", "type": "Sensor", "cost": 500},
        {"id": 102, "name": "B", "type": "Sensor", "cost": 100},
        {"id": 103, "name": "C", "type": "Sensor", "cost": 500}
    ]

    result = sort_by_cost(inventory)

    assert [equipment["cost"] for equipment in result] == [100, 500, 500]