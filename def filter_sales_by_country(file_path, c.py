file_path ="SalesJan2009.csv"

def filter_sales_by_country(file_path, country):
    with open(file_path, "r", encoding="utf-8") as file:
        header = file.readline().strip().split(",")  # Leer encabezado
        country_index = header.index("Country")  # Obtener índice de la columna "Country"
        sales = []
        
        for line in file:
            data = line.strip().split(",")
            if data[country_index] == country:
                sales.append(data)
        
    return sales

# Ruta del archivo
country = "United States"  # Cambia esto al país deseado

# Obtener las compras
sales_in_country = filter_sales_by_country(file_path, country)

# Mostrar los resultados
for sale in sales_in_country[:5]:  # Muestra las primeras 5 ventas
    print(sale)
