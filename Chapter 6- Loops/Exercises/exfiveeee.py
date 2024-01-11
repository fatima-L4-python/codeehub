sandwich_orders = [
    'pastrami', 'veggie', 'grilled cheese', 'pastrami',
    'chicken', 'roast beef', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("Your " + current_sandwich + " sandwich is being made.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("Your " + sandwich + " sandwich is ready.")