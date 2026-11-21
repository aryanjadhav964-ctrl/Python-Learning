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


#### question 2 : lead grouping and frequency counter [Dynamic Dictionary Building] ####
# Your Adhyatma Yoga website collected raw lead submissions throughout the day, stored as a list of dictionaries. Some inquiries are missing a "source" key.

# task 
# Build a dictionary named batch_counts that dynamically counts how many leads requested each batch (e.g., {'morning': 3, 'evening': 1, 'weekend': 1}).

# Create a list named instagram_leads containing only the names ("Sneha", "Priya") of leads who came from "Instagram". (Hint: Use .get("source") so your code doesn't throw a KeyError on leads missing the "source" key!)

# Print batch_counts and instagram_leads.

raw_leads = [
    {"name": "Rohan", "batch": "morning"},
    {"name": "Sneha", "batch": "evening", "source": "Instagram"},
    {"name": "Amit", "batch": "morning", "source": "Google"},
    {"name": "Priya", "batch": "morning", "source": "Instagram"},
    {"name": "Karan", "batch": "weekend"}
]

# batch counting #
batch_count = {
    "morning" : 0,
    "evening" : 0,
    "weekends" : 0
}

for x in raw_leads:
    if x["batch"] == "morning":
        batch_count["morning"] = batch_count["morning"]+1
    elif x["batch"] == "evening":
        batch_count["evening"] = batch_count["evening"]+1
    else:
        batch_count["weekends"] = batch_count["weekends"]+1


# separating leads according to their source  # 
instagram_leads = []

for x in raw_leads:
    if x.get("source") == "Instagram":
        instagram_leads.append(x["name"])

print(batch_count)
print(f"From Instagram : {instagram_leads}")