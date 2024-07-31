from flask import Blueprint, request, jsonify, session
from app import db
from app.models import Item, Expense
import datetime

main = Blueprint('main', __name__)

@main.route('/items', methods=['POST'])
def create_item():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    data = request.get_json()
    new_item = Item(name=data['name'], description=data.get('description'))
    db.session.add(new_item)
    db.session.commit()
    return jsonify(new_item.to_dict()), 201

@main.route('/items', methods=['GET'])
def get_items():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

@main.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    item = Item.query.get_or_404(id)
    return jsonify(item.to_dict())

@main.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    data = request.get_json()
    item = Item.query.get_or_404(id)
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    db.session.commit()
    return jsonify(item.to_dict())

@main.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return '', 204



#Expense Routes are here
@main.route('/expenses', methods=['POST'])
def create_expense():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    data = request.get_json()
    date_str = data['date']
    try:
        date = datetime.date.fromisoformat(date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
    
    new_expense = Expense(
        date=date,
        description=data['description'],
        amount=data['amount']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201

@main.route('/expenses', methods=['GET'])
def get_expenses():
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    expenses = Expense.query.all()
    return jsonify([expense.to_dict() for expense in expenses])

@main.route('/expenses/<int:id>', methods=['GET'])
def get_expense(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401

    expense = Expense.query.get_or_404(id)
    return jsonify(expense.to_dict())

@main.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401

    data = request.get_json()
    expense = Expense.query.get_or_404(id)
    try:
        date = datetime.date.fromisoformat(data.get('date', expense.date.isoformat()))
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    expense.date = date
    expense.description = data.get('description', expense.description)
    expense.amount = data.get('amount', expense.amount)
    db.session.commit()
    return jsonify(expense.to_dict())

@main.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    if 'user_id' not in session:
        return jsonify({"message": "Unauthorized!"}), 401
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return '', 204