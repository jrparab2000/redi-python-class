def print_starting():
    print("Shopping Cart Calculator")
    print("========================")
    print()

def get_input():
    item = input(f"Enter item name (or 'checkout' to finish): ")
    return item

def get_price():
    price = float(input(f"Enter price: "))
    print()
    return price

def apply_discount(total):
    if total > 1000:
        return 0.1*total
    return 0

def print_receipt(items):
    print("RECEIPT")
    print("=======")
    total = float(0)
    for key, value in items.items():
        print(f"{key}\t\t\t${value}")
        total = total + value
    print(f"\t\t\t\t--------")
    print(f"Subtotal:\t\t\t${total:.2f}")
    disc_total = apply_discount(total)
    print(f"Discount (10% for $1000+):\t-${disc_total:.2f}")
    total = total - disc_total
    tax = total*0.085
    total = total + tax
    print(f"Tax (8.5%):\t\t\t${tax:.2f}")
    print(f"Shipping:\t\t\t$9.99")
    print(f"\t\t\t\t--------")
    total = total + 9.99
    print(f"TOTAL:\t\t\t\t${total:.2f}")

def main():
    print_starting()
    items = {}
    while True:
        item = get_input()
        if item.lower() == "checkout":
            break
        price = get_price()
        items[item] = price
    print_receipt(items)

if __name__ == "__main__":
    main()