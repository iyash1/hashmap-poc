# Simple in-memory HashMap CLI utility
hashmap = {}
menu_options = {
    1: 'Add / Update',
    2: 'Search',
    3: 'Delete',
    4: 'Show records',
    5: 'Exit'
}

# Create a HashMap to store data
def create_hashmap(initial_size=8):
    """
    Initialize a new hash map structure with a given number of buckets.
    Fields:
      - size: number of buckets
      - count: number of stored key-value pairs
      - buckets: list of bucket lists for separate chaining
    """
    global hashmap
    hashmap = {
        "size": initial_size,
        "count": 0,
        "buckets": [[] for _ in range(initial_size)]
    }

# Hash function to get bucket index
def hash_key(key, size):
    """
    Compute bucket index for a key using Python's built-in hash.
    """
    return hash(key) % size

def load_factor(hm):
    """
    Return current load factor (count / size).
    """
    return hm["count"] / hm["size"]


def resize(hm):
    """
    Double the number of buckets and rehash all existing entries.
    """
    old_buckets = hm["buckets"]
    new_size = hm["size"] * 2

    hm["size"] = new_size
    hm["buckets"] = [[] for _ in range(new_size)]
    hm["count"] = 0

    for bucket in old_buckets:
        for key, value in bucket:
            store_data(key, value)

# Prompt helper for asking whether to continue an operation
def continue_prompt(menu=None):
    if menu is None:
        print("Invalid menu option. Please select a valid option.")
        return menu

    more = input(f"Do you want to {menu_options[menu]} in hashmap? (y/n): ")
    if more not in ("y", "n"):
        return 'Invalid input. Please enter \'y\' or \'n\'.'
    else:
        return more

# Add or update an entry in the hashmap (handles resizing)
def store_data(key, name):
    if load_factor(hashmap) > 0.7:
        resize(hashmap)

    bucket_index = hash_key(key, hashmap["size"])
    bucket = hashmap["buckets"][bucket_index]
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, name)
            print(f"Updated entry: ID = {key}, Name = {name}")
            return
    bucket.append((key, name))
    hashmap["count"] += 1
    print(f"Added entry: ID = {key}, Name = {name}")

# Input loop for adding/updating entries
def input_menu():
    accept_values = continue_prompt(1)
    print(accept_values)
    while accept_values == 'y':
        try:
            key = int(input("Enter ID (Number) : "))
            name = input("Enter Full Name : ")
            store_data(key, name)
        except ValueError:
            print("Invalid input. Please enter a valid number for ID.")
            continue
        accept_values = continue_prompt(1)

# Input loop for searching by key
def search_menu():
    accept_values = continue_prompt(2)
    while accept_values == 'y':
        try:
            search_key = int(input("Enter ID to search: "))
            bucket_index = hash_key(search_key, hashmap["size"])
            bucket = hashmap["buckets"][bucket_index]
            for k, v in bucket:
                if k == search_key:
                    print(f"Found: ID = {k}, Name = {v}")
                    return
            print("ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number for ID.")
        accept_values = continue_prompt(2)

# Print the current hashmap contents and stats
def print_hashmap():
    """
    Display hashmap size, count, and non-empty buckets.
    """
    global hashmap
    print(f"HashMap Size: {hashmap['size']}; Count: {hashmap['count']}")
    for i, bucket in enumerate(hashmap["buckets"]):
        if bucket:
            print(f"Bucket {i}: {bucket}")

# Delete an entry by key
def delete_data():
    try:
        key = int(input("Enter ID to delete: "))
        bucket_index = hash_key(key, hashmap["size"])
        bucket = hashmap["buckets"][bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                hashmap["count"] -= 1
                print(f"Deleted entry with ID = {key} and Value = {v}")
                return
        print("ID not found. No entry deleted.")
    except ValueError:
        print("Invalid input. Please enter a valid number for ID.")

# Main menu loop for operations
def operations_menu():
    while True:
        print("\nMenu Options:")
        for key, value in menu_options.items():
            print(f"{key}. {value}")
        try:
            choice = int(input("Select an option: "))
            if choice == 1:
                input_menu()
            elif choice == 2:
                search_menu()
            elif choice == 3:
                delete_data()
            elif choice == 4:
                print_hashmap()
            elif choice == 5:
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a valid menu option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")

# Main execution
if __name__ == "__main__":
    print("Welcome to HashMap CLI")
    create_hashmap()
    operations_menu()
    print("Final HashMap Data:")
    print_hashmap()