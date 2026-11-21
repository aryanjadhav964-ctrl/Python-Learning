# Problem 1: Low-Stock Filter & Summary (Lists of Dictionaries)
# In Inventra, database queries return a list of dictionaries where each dictionary represents a product.

# your task :
 
# Create an empty list called low_stock_alerts.

# Loop through inventory. If an item's "stock" is less than 5, append a formatted string to low_stock_alerts like "Galaxy Z Fold 6 (Only 2 left)".

# Calculate the total monetary value of all items currently in stock (stock * price summed across all products) and store it in total_inventory_value.

# Print both low_stock_alerts and total_inventory_value.

#### inventory items ####
inventory = [
    {"sku": "LAP-01", "model": "ASUS Vivobook S14", "stock": 12, "price": 68000},
    {"sku": "MOB-04", "model": "Galaxy Z Fold 6", "stock": 2, "price": 164999},
    {"sku": "LAP-02", "model": "MacBook Air M3", "stock": 4, "price": 114900},
    {"sku": "MOB-09", "model": "Pixel 9 Pro", "stock": 9, "price": 109999}
]

# Empty list 
low_stock_alerts = []

## loop to check low stock in inventory ###
for x in inventory:
    if x["stock"] <= 5 :
        low_stock_alerts.append(x)

### formating low stock items to display ####
for x in low_stock_alerts:
    print(f"{x["model"]} (only {x["stock"]} left)")


