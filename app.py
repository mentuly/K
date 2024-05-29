from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = [
        {'name': 'Margherita', 'ingredients': 'Tomato, Mozzarella, Basil', 'price': '8.99'},
        {'name': 'Pepperoni', 'ingredients': 'Tomato, Mozzarella, Pepperoni', 'price': '9.99'},
        {'name': 'Hawaiian', 'ingredients': 'Tomato, Mozzarella, Ham, Pineapple', 'price': '10.99'},
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)