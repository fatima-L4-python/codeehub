sandwich_orders = ['veggie', 'cheese', 'chicken', 'beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Your " + current_sandwich + " sandwich is being made.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " sandwich is ready.")