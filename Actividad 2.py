file_path = "SalesJan2009.csv"
def filter_sales_by_payment_type(file_path, payment_type):
    with open(file_path, "r", encoding="utf-8") as file:
        header = file.readline().strip().split(",")  # Leer encabezado
        payment_index = header.index("Payment_Type")  # Obtener índice de la columna "Payment_Type"
        sales = []
        
        for line in file:
            data = line.strip().split(",")
            if data[payment_index] == payment_type:
                sales.append(data)
        
    return sales

# Ruta del archivo
payment_type = "Visa"  # Cambia esto al medio de pago deseado

# Obtener las compras
sales_by_payment = filter_sales_by_payment_type(file_path, payment_type)

# Mostrar los resultados
for sale in sales_by_payment[:5]:  # Muestra las primeras 5 ventas
    print(sale)