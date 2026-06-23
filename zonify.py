import csv
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

def clasificar_y_leer_csv():
    averias_cnfl = []
    cortes_aya = []
    eventos_cosevi = []

    try:
        with open('Accidentes.csv', mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                tipo = fila['tipo_accidente'].strip()
                desc = fila['descripcion']
                fecha = fila['fecha_hora']
                
                if tipo == "Corte de luz":
                    item = {
                        'id': f"INC-{fila['id']}",
                        'zona': f"{fila['canton']}, {fila['provincia']}",
                        'causa': desc,
                        'direccion': fila['ruta'],
                        'fecha': fecha,
                        'clientes_afectados': "N/D"
                    }
                    averias_cnfl.append(item)
                    
                elif tipo == "Corte de agua":
                    item = {
                        'id': f"INC-{fila['id']}",
                        'zona': f"{fila['canton']}, {fila['provincia']}",
                        'causa': desc,
                        'direccion': fila['ruta'],
                        'fecha': fecha,
                        'clientes_afectados': "N/D"
                    }
                    cortes_aya.append(item)
                    
                else:
                    evento_cosevi = {
                        'anio': fecha.split('-')[0] if '-' in fecha else "2026",
                        'tipo': tipo,
                        'ruta': fila['ruta'],
                        'canton': fila['canton'],
                        'provincia': fila['provincia'],
                        'fuente': "MOPT / COSEVI" if tipo == "Accidente" else "Reporte de Tránsito",
                        'descripcion': desc,
                        'fecha_hora': fecha
                    }
                    eventos_cosevi.append(evento_cosevi)

    except Exception as e:
        print(f"Error leyendo el CSV: {e}")
        
    return averias_cnfl, cortes_aya, eventos_cosevi

@app.route('/')
def home():
    cnfl, aya, cosevi = clasificar_y_leer_csv()
    return render_template('index.html', 
                           averias=cnfl, 
                           cortes=aya, 
                           eventos=cosevi, 
                           total_clientes=len(cnfl))

@app.route('/actualizar')
def actualizar():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)