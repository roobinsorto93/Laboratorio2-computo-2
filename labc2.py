
import pandas as pd
 

df = pd.read_csv(r"Analyzing_Student_Academic_Trends.csv")


print("===== RESUMEN ESTADÍSTICO DEL DATASET =====")
print(df.describe(include='all'))
 

print("\n===== TIPOS DE DATOS =====")
print(df.dtypes)
 
print("""
Interpretación:
- Las columnas numéricas (int64, float64) permiten calcular medidas como media, mediana y desviación estándar.
- Las columnas tipo object (texto) permiten análisis categóricos (valores únicos, conteos, etc.).
""")
 
print("\n===== PRIMEROS 5 REGISTROS =====")
print(df.head())
 
print("\n===== ÚLTIMOS 5 REGISTROS =====")
print(df.tail())
 
if 'GPA' in df.columns:
    print("\n===== ORDENADO POR GPA (MAYOR A MENOR) =====")
    print(df.sort_values(by='GPA', ascending=False).head(10))
else:
    print("\nNo se encontró la columna 'GPA', se usará otra columna numérica disponible.")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        print(f"\nOrdenando por la columna: {col}")
        print(df.sort_values(by=col, ascending=False).head(10))
    else:
        print("No hay columnas numéricas para ordenar.")
 

columna_objetivo = 'GPA' if 'GPA' in df.columns else df.select_dtypes(include=['int64', 'float64']).columns[0]
 
media = df[columna_objetivo].mean()
mediana = df[columna_objetivo].median()
desviacion = df[columna_objetivo].std()
 
print(f"\n===== MEDIDAS ESTADÍSTICAS DE '{columna_objetivo}' =====")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
 

print(f"""
Conclusión:
La columna analizada fue '{columna_objetivo}'.
- Una media cercana a la mediana sugiere una distribución equilibrada.
- Una desviación estándar alta indica gran variabilidad entre los valores.
- Si se observa la lista ordenada, podemos identificar los estudiantes o categorías con mejores resultados.
""")