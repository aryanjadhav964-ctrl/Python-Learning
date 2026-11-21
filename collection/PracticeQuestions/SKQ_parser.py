#Problem 2: API Endpoint & SKU Parser (String Slicing, Splitting & Case Formatting)

raw_api_path = "  /api/v1/inventory/LAP-dell_xps15-2026-in_stock/  "

clean_path = raw_api_path.strip().strip("/")

path_sagment = clean_path.split("/")

sku_path = path_sagment[-1]

sku_parts = sku_path.split("-")

category_code = sku_parts[0][:3]
model_name = sku_parts[1].replace("_", " ")
batch_year = int(sku_parts[2])
status = sku_parts[3].replace("_", " ").title()

product_data = {
    "category_code" : category_code,
    "model_name" : model_name,
    "batch_year" : batch_year,
    "status" : status
}
print(product_data)