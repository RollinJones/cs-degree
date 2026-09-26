def add_equipment(inventory, new_equipment):
    for equipment in inventory:
        if equipment['id'] == new_equipment['id']:
            return False
    inventory.append(new_equipment)
    return True

def delete_equipment(inventory, equipment_id):
    for index, equipment in enumerate(inventory):
        if equipment['id'] == equipment_id:
            del inventory[index]
            return True
    return False

def update_equipment(inventory, equipment_id, updated_equipment):
    for index, equipment in enumerate(inventory):
        if (equipment['id'] == equipment_id and updated_equipment['id'] == equipment_id):
            inventory[index] = updated_equipment
            return True
    return False

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

    new_equipment = {
        "id": 106,
        "name": "Flow Meter",
        "type": "Sensor",
        "cost": 2500
    }

    updated_equipment = {
        "id": 103,
        "name": "Pressure Transmitter",
        "type": "Sensor",
        "cost": 950
    }

    ### result = add_equipment(inventory, new_equipment)
    ### result = delete_equipment(inventory, 103)
    result = update_equipment(inventory, 103, updated_equipment)
    print(result)
    print(inventory)

### print(inventory[2])
### 
### inventory[1]["cost"] = 15000
### print(inventory[1])
### 
### inventory.append({
###     "id": 106,
###     "name": "H2S Scrubber",
###     "type": "Vessel",
###     "cost": 35000 
### })
### print(inventory)
### 
### for equipment in inventory:
###     print(f"{equipment['name']}: ${equipment['cost']}")