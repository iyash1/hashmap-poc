hashmap = {}
menu_options = {
    1: 'Add / Update',
    2: 'Search',
    3: 'Delete',
    4: 'Exit'
}

def create_hashmap(initial_size=8):
    """
    Create a new hash map with given number of buckets.
    """
    global hashmap
    hashmap = {
        "size": initial_size,                 # number of buckets
        "count": 0,                            # number of key-value pairs
        "buckets": [[] for _ in range(initial_size)]
    }


def hash_key(key, size):
    """
    Convert a key into a bucket index.
    """
    return hash(key) % size

def continue_prompt(menu=None):
    if menu is None:
        print("Invalid menu option. Please select a valid option.")
        return menu
    
    more = input(f"Do you want to {menu_options[menu]} in hashmap? (y/n): ")
    if more not in ("y", "n"):
        return 'Invalid input. Please enter \'y\' or \'n\'.'
    else:
        return more

def store_data(key, name):
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
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please select a valid menu option.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")


if __name__ == "__main__":
    print("Welcome to HashMap CLI")
    create_hashmap()
    operations_menu()
    print("Final HashMap Data:")
    print(f"Total Buckets: {hashmap['size']}; Total Entries: {hashmap['count']}")
    print(f"HashMap Contents: {hashmap['buckets']}")