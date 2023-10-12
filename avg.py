sales = [
    {"sales_one": [23, 45, 76, 48]},
    {"sales_two": [44, 20, 17, 34]},
    {"sales_three": [89, 32, 12, 34]}
]

# Calculate the average for each sale
averages = {}
all_sale = []


for sale_data in sales:
    for sale_name, sale_values in sale_data.items():
        avg = sum(sale_values) / len(sale_values)
        averages[sale_name] = avg
        all_sale.extend(sale_values)

# total averages
total_avarage = sum(all_sale) / len(all_sale)

# Print the averages
for sale_name, avg in averages.items():
    print(f"Average for {sale_name}: {avg}")
    
print(all_sale)
print(f'Total avarage: {total_avarage}')
