from equipment_inventory.inventory import add_equipment, delete_equipment, update_equipment

def test_add_equipment():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500}
    ]

    new_equipment = {
        "id": 102,
        "name": "Gas Blower",
        "type": "Blower",
        "cost": 12000
    }

    result = add_equipment(inventory, new_equipment)

    assert result is True
    assert len(inventory) == 2
    assert inventory[1] == new_equipment


def test_add_equipment_empty_inventory():
    inventory = []

    new_equipment = {
        "id": 101,
        "name": "H2S Analyzer",
        "type": "Sensor",
        "cost": 4500
    }

    result = add_equipment(inventory, new_equipment)

    assert result is True
    assert inventory == [new_equipment]


def test_add_duplicate_id():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500}
    ]

    duplicate = {
        "id": 101,
        "name": "Different Analyzer",
        "type": "Sensor",
        "cost": 5000
    }

    result = add_equipment(inventory, duplicate)

    assert result is False
    assert len(inventory) == 1

def test_delete_equipment():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500},
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000}
    ]

    result = delete_equipment(inventory, 101)

    assert result is True
    assert len(inventory) == 1
    assert inventory[0]["id"] == 102


def test_delete_missing_equipment():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500}
    ]

    result = delete_equipment(inventory, 999)

    assert result is False
    assert len(inventory) == 1


def test_delete_from_empty_inventory():
    inventory = []

    result = delete_equipment(inventory, 101)

    assert result is False
    assert inventory == []

def test_update_equipment():
    inventory = [
        {"id": 101, "name": "H2S Analyzer", "type": "Sensor", "cost": 4500},
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000}
    ]
    updated_equipment = {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 9000}
    result = update_equipment(inventory, 102, updated_equipment)

    assert result is True
    assert inventory[1]["cost"] == 9000


def test_update_missing_equipment():
    inventory = [
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000}
    ]
    updated_equipment = {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 9000}
    result = update_equipment(inventory, 999, updated_equipment)

    assert result is False


def test_update_from_empty_inventory():
    inventory = []
    updated_equipment = {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 9000}
    result = update_equipment(inventory, 102, updated_equipment)

    assert result is False
    assert inventory == []

def test_update_cannot_change_id():
    inventory = [
        {"id": 102, "name": "Gas Blower", "type": "Blower", "cost": 12000}
    ]

    updated_equipment = {
        "id": 999,
        "name": "Gas Blower",
        "type": "Blower",
        "cost": 9000
    }

    result = update_equipment(inventory, 102, updated_equipment)

    assert result is False
    assert inventory[0]["id"] == 102