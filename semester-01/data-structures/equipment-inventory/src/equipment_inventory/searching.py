def search_by_id(inventory, equipment_id):
    for equipment in inventory:
        if equipment['id'] == equipment_id:
            return equipment
    return None

def search_by_type(inventory, equipment_type):
    matches = []
    for equipment in inventory:
        if equipment['type'] == equipment_type:
            matches.append(equipment)
    return matches

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

    ### result = search_by_id(inventory, 99)
    ### result = search_by_type(inventory, "Vessel")
    ### print(result)