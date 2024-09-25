from app import create_app

# Crear una instancia de la aplicación
app = create_app()

if __name__ == '__main__':
    # Ejecutar la aplicación en todas las interfaces de red
    app.run(debug=False,host="0.0.0.0")
