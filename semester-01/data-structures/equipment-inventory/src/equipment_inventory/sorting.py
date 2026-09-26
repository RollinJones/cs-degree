def sort_by_cost(inventory):
    length = range(len(inventory) - 1)
    for i in length:
        position = i + 1
        key = inventory[position]
        while position > 0 and key['cost'] < inventory[position - 1]['cost']:
            inventory[position] = inventory[position-1]
            position -= 1
        inventory[position] = key    
    return inventory
        
if __name__ == "__main__":

    inventory = [
        {
            "id": 101,
            "name": "H2S Analyzer",
            "type": "Sensor",
            "cost": 4500
        },
        {
            "id": 102,
            "name": "Gas Blower",
            "type": "Blower",
            "cost": 12000
        },
        {
            "id": 103,
            "name": "Pressure Transmitter",
            "type": "Sensor",
            "cost": 850
        },
        {
            "id": 104,
            "name": "Feed Pump",
            "type": "Pump",
            "cost": 3200
        },
        {
            "id": 105,
            "name": "Temperature Probe",
            "type": "Sensor",
            "cost": 450
        },
        {
            "id": 106,
            "name": "H2S Scrubber",
            "type": "Vessel",
            "cost": 35000 
        }
    ]
    
    insertion_inventory = inventory.copy()
    builtin_inventory = inventory.copy()

    insertion_result = sort_by_cost(insertion_inventory)

    sorted_result = sorted(
        builtin_inventory,
        key=lambda equipment: equipment["cost"]
    )

    print(insertion_result)
    print(sorted_result)

    print(insertion_result == sorted_result)