from tabulate import tabulate

table=[
    ["cesar mayta","cesarmayta@gmail.com","987456123"],
    ["cesar mayta","cesarmayta@gmail.com","987456123"]
]

columnas=["nombre","email","celular"]

print(tabulate(table,headers=columnas))