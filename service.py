from models import User
from schema import Usercreateshcema,Userdeletescheme,GetUserschema,UpdateUserschema
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException

def create_user_in_db(data:Usercreateshcema,db:Session):
    new_user=User(username=data.username,password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"new user is created"}

def delete_user_in_db(data:Userdeletescheme,db:Session):
    user_in_db= db.query(User).filter(User.username==data.username).first()
    if not user_in_db:
        raise UserNotFoundException
    db.delete(user_in_db)
    db.commit()
    return {"msg":"user is deleted"}

def get_user_from_db(*,username:str,db:Session):
    user_from_db=db.query(User).filter(User.username==username).first()
    if not user_from_db:
        raise UserNotFoundException
    else:
        message={"username":user_from_db.username,"password":user_from_db.password}
        return message

def update_user_from_db(user_name:str,new_username:str,data: UpdateUserschema,db:Session):
    user_db=db.query(User).filter_by(username=user_name , password=data.password).first()
    if not user_db:
        raise UserNotFoundException
    user_db.username=new_username
    db.commit()
    db.refresh(user_db)
    return {"message":"username is updated succesfully"}
    