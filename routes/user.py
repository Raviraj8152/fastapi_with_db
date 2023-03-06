from fastapi  import APIRouter
import pymongo
from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from pymongo import MongoClient

user = APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity( conn.local.user.find())

@user.get('/{id}')
async def find_all_user(id):
    #  return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))
    return {"data":" no you are here ",
            "urid":id} 


@user.post('/')
async def create_user(user:User):
    conn.local.user.insert_one(dict(user))
    return {"data":"you have registered"}



@user.put('/{id}')
async def update_user(id, user:User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(user)})
    return userEntity(conn.local.user,find_all_user({"_id": ObjectID(id)}))

@user.delete('/{id}')
async def delete_user(id, user:User):
    return userEntity(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))




