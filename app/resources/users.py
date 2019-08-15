from sanic import response, Blueprint
from sanic.exceptions import NotFound
from sanic_openapi import doc

from models.users import User
from swagger_config import UserBody, UserOne, UserList

user_bp = Blueprint('user', url_prefix='/users')


@user_bp.route("/")
@doc.summary("Find all users.")
@doc.description('Query all users data from database')
@doc.produces(UserList)
async def get_all_users(request):
    users = User.find_all()
    if not users:
        raise NotFound("Data not found.")
    data = [{"id": u.id, "username": u.username, "password": u.password} for u in users]
    return response.json({"data": data})


@user_bp.route("/<user_id:int>")
@doc.summary("Find one user.")
@doc.description('Query one user data by ID from database')
@doc.produces(UserOne)
async def get_user(request, user_id):
    user = User.find_by_user_id(user_id)
    if not user:
        raise NotFound("Data not found.") 
    data = {"id": user.id, "username": user.username, "password": user.password}
    return response.json({"data": data})


@user_bp.route("/", methods=['POST'])
@doc.summary("Create a new user.")
@doc.description('Insert one user data into database')
@doc.consumes(UserBody, location="body")
@doc.produces(UserOne)
async def create_user(request):
    json_data = request.json
    username = json_data.get('username', None)
    password = json_data.get('password', None)
    if not username or not password:
        raise ValueError
    user = User.create_user(username, password)
    data = {"id": user.id, "username": user.username, "password": user.password}
    return response.json({"data": data})
    

@user_bp.route("/<user_id:int>", methods=['PUT'])
@doc.summary("Update a user data.")
@doc.description('Update one user data by ID into database')
@doc.consumes(UserBody, location="body")
@doc.produces(UserOne)
async def update_user(request, user_id):
    json_data = request.json
    if not json_data:
        raise ValueError
    user = User.update_by_id(user_id, json_data)
    data = {"id": user.id, "username": user.username, "password": user.password}
    return response.json({"data": data})

    
@user_bp.route("/<user_id:int>", methods=['DELETE'])
@doc.summary("Delete a user.")
@doc.description('Delete one user data by ID from database')
@doc.produces(UserOne)
async def delete_user(request, user_id):
    
    user = User.find_by_user_id(user_id)
    if not user:
        raise NotFound("Data not found.")
    User.delete_by_id(user_id)
    data = {"id": user.id, "username": user.username, "password": user.password}
    return response.json({"data": data})