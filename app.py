from fastapi import FastAPI
import json

dict_ = {}
with open("contacts_api.json", "r") as f:
    data = f.read()
    dict_ = json.loads(data)

app = FastAPI()

#  WORKING PROGRAM WITH SINGLE INPUT
@app.get("/Add_contact")
def Add_Or_Update_a_Contact(Name: str, Number: int):

    dict_[Name.capitalize()] = Number
    with open("contacts_api.json", "w+") as f:
        f.write(json.dumps(dict_))

    return dict_


@app.delete("/Delete_contact")
def Delete_a_contact(name: str):
    Name = name.capitalize()

    if Name in dict_:
        del dict_[Name]
    with open("contacts_api.json", "w+") as f:
        f.write(json.dumps(dict_))

    return Name


@app.post("/View_contacts")
def View_all_contacts():
    return dict_


@app.get("/Search_contact")
def Search_a_contact(name: str):
    Name = name.capitalize()
    if Name in dict_:
        return Name, dict_[Name]