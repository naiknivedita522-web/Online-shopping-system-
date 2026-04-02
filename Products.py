products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Keyboard", "price": 1500}
}

def show_products():
    print("\nAvailable Products:")
    for pid, details in products.items():
        print(f"{pid}. {details['name']} - ₹{details['price']}")
