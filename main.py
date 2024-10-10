from fastapi import FastAPI,Depends
from db import get_db
from sqlalchemy.orm import Session
from schema import Usercreateshcema,Userdeletescheme,GetUserschema,UpdateUserschema
from service import create_user_in_db,delete_user_in_db,get_user_from_db,update_user_from_db
app = FastAPI()


@app.get("/")
def healthy_check():
    return {"msg":"this is my site"}

@app.post("/user")
def create_user(item: Usercreateshcema,db:Session=Depends(get_db)):
    message=create_user_in_db(data=item,db=db)
    return message

@app.delete("/user")
def delete_user(item:Userdeletescheme,db:Session=Depends(get_db)):
    message=delete_user_in_db(data=item,db=db)
    return message

@app.get("/user")
def get_user(username:str, db:Session=Depends(get_db)):
    user=get_user_from_db(username=username,db=db)
    return user

@app.put("/user")
def update_user(username:str,new_username:str,item:UpdateUserschema ,db:Session=Depends(get_db)):
    user=update_user_from_db(user_name=username,new_username=new_username,data=item,db=db)
    return user    