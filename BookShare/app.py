from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

categories = [
    {
    'name':'technology',
    'items':[
        {
        'name':'Effective Python',
        'price':20.99
        }
    ]
    }
]

#POST - used to receive data
#GET - used to send data back only

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/category', methods=['POST'])
def create_category():
    request_data = request.get_json()
    new_category = {
        'name':request_data['name'],
        'items':[]
    }
    categories.append(new_category)
    return jsonify(new_category)

@app.route('/category/<string:name>')
def get_category(name):
    #Iterate over categories
    #If the name matches, return it
    #If not, return an error message
    for category in categories:
        if category['name'] == name:
            return jsonify(category)
        else:
            return jsonify({'message':'category not found'})

@app.route('/category')
def get_categories():
    return jsonify({'categories': categories}) #have to be dictionary cant list only

@app.route('/category/<string:name>/item', methods=['POST'])
def add_book(name):
    request_data=request.get_json()
    for category in categories:
        if category['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            category['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'category not found'})

@app.route('/category/<string:name>/item')
def get_books_in_store(name):
    for category in categories:
        if category['name'] == name:
            return jsonify({'items':category['items']})
    return jsonify({'message':'store not found'})


app.run(port=5000)
