#!/usr/bin/env python
"""
    Обработка формы вывода списка абитуриентов
"""



import cgitb
import cgi
import json

from univ import (
    Univ,
    UnivException
)



cgitb.enable()
print("Content-Type: text/html; charset=utf-8\n")



univ = Univ()
form = cgi.FieldStorage()
response = {
    "status": "bad",
    "message": "Ошибка при получении списка абитуриентов !"
}

isDocHighScore = form.getfirst("isDocHighScore").lower() == "true"
isHostel = form.getfirst("isHostel").lower() == "true"
isExternal =form.getfirst("isExternal").lower() == "true"
isAllHighScore = form.getfirst("isAllHighScore").lower() == "true"

groups = []
if isDocHighScore:
    groups.append("isDocHighScore")
if isHostel:
    groups.append("isHostel")
if isExternal:
    groups.append("isExternal")
if isAllHighScore:
    groups.append("isAllHighScore")

response["students"] = [student for student in univ.get_students(groups)]
response["status"] = "ok"

univ.close()
print(json.dumps(response, ensure_ascii=False))
