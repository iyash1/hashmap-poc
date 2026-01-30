# HashMap CLI

Simple in-memory HashMap CLI implemented in Python. Supports add/update, search, delete, and display of entries using integer keys and string values. Automatically resizes (rehashes) when load factor exceeds 0.7.

## Features
- Create a HashMap with configurable bucket count (default 8)
- Add or update entries (ID -> Full Name)
- Search by ID
- Delete by ID
- Show records (print non-empty buckets and stats)
- Automatic resizing (doubling buckets) when load factor > 0.7
- Interactive menu-driven CLI

## Requirements
- Python 3.12

## Usage
Save the script (e.g. `hashmap_cli.py`) and run:

```bash
python3 hashmap_cli.py
```

Typical interactive flow:
- Select menu option:
    - 1 Add / Update
    - 2 Search
    - 3 Delete
    - 4 Show records
    - 5 Exit
- For Add/Update and Search the CLI will prompt to continue (y/n).

## Key functions
- create_hashmap(initial_size=8) — initialize buckets, count and size
- hash_key(key, size) — map key to bucket index
- load_factor(hm) — return current load factor (count / size)
- resize(hm) — double buckets and rehash all entries
- store_data(key, name) — insert or update a (key, name) pair (triggers resize)
- input_menu(), search_menu(), delete_data(), print_hashmap(), operations_menu() — interactive handlers

## Data layout
The HashMap structure:
```py
{
        "size": <num_buckets>,
        "count": <num_entries>,
        "buckets": [ [(k,v), ...], ... ]  # list of bucket lists (separate chaining)
}
```

## Notes
- Keys are integers; invalid ID inputs are handled with a prompt.
- Uses Python's built-in hash modulo bucket count for bucket selection.
- Resizes (rehashes) when load factor exceeds 0.7 to maintain performance.
- No persistence; data is lost on program exit.
- "Show records" prints HashMap size, count, and non-empty buckets.
