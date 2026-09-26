### ### Lists and Dictionaries

I used a list to store the equipment inventory, with each individual equipment record stored as a dictionary containing an ID, name, equipment type, and cost. I completed functions to add, update, and delete equipment. Retrieving equipment by ID is handled by the `search_by_id()` function in the searching portion of the project.

The add function prevents duplicate equipment IDs. The update function identifies an equipment record by ID and replaces the existing dictionary while preventing the equipment ID from being changed. The delete function searches for the equipment ID and removes the matching record.

### Searching

I implemented linear search functions for searching by equipment ID and equipment type.

Both functions have O(n) worst-case time complexity because they may need to examine every equipment record in the inventory.

`search_by_id()` can stop as soon as the matching ID is found because equipment IDs are unique. `search_by_type()` must search the entire inventory because multiple equipment records can have the same type.

### Sorting

I implemented insertion sort to sort the inventory from lowest to highest equipment cost. I compared the result of my insertion sort with Python's built-in `sorted()` function and confirmed that they produced the same ordering.

Insertion sort has O(n²) worst-case time complexity because each item may need to be compared with and shifted past many previous items. Its best-case time complexity is O(n) when the inventory is already sorted.

Python's built-in `sorted()` is more efficient for general use and has O(n log n) worst-case time complexity. My insertion sort modifies the provided list, while `sorted()` returns a new sorted list.

### Testing and Documentation

I used pytest to test the inventory, searching, and sorting functions. The tests cover normal operations, empty collections, duplicate IDs, missing records, attempts to change an equipment ID during an update, already-sorted inventories, reverse-sorted inventories, and duplicate equipment costs.

All tests pass successfully.

| Function / Operation |                                  Time Complexity | Why                                                                                                                                                           |
| -------------------- | -----------------------------------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `add_equipment()`    |                                         **O(n)** | You scan the inventory to check for duplicate IDs before appending. The append itself is usually O(1), but the duplicate check makes the whole function O(n). |
| `update_equipment()` |                                         **O(n)** | In the worst case, you search through the entire list before finding the ID or determining it is missing.                                                     |
| `delete_equipment()` |                                         **O(n)** | You may search the whole list, and deleting from the middle of a list can also require shifting later elements.                                               |
| `search_by_id()`     |                              **O(n)** worst case | It can stop early if it finds the ID, but the ID could be last or missing.                                                                                    |
| `search_by_type()`   |                                         **O(n)** | You need to inspect the entire inventory because multiple records may match the same type.                                                                    |
| `sort_by_cost()`     | **O(n²)** worst/average case, **O(n)** best case | Insertion sort may repeatedly shift each item through much of the already-sorted portion.                                                                     |
| Python `sorted()`    |                        **O(n log n)** worst case | Python uses Timsort, which is generally much more efficient than insertion sort on large collections.                                                         |
