import pandas as pd
import matplotlib.pyplot
# Ricardo Lopez
# 1. leer el archivo CSV comida oais india
df_food_india = pd.read_csv('indian_food.csv')

print("DATOS LEIDOS DESDE VSC, comida india 0085")
print(df_food_india)
print("mostrar nombre comida + ingredientes 0085")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("tiempo de cocinado mostrar 10 registrar con head 0085")
nombre_y_hora=df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)