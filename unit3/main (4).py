def linear_search_product(product_list, target_product):
  indices = []
  for i in range(len(product_list)):
    if product_list[i] == target_product:
      indices.append(i)
  return indices


# Example list of products
products = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]

# Target product to search for
target_product = "Apple"

# Call the function to find indices of the target product
indices = linear_search_product(products, target_product)

# Print the result
print("Indices of", target_product, ":", indices)
