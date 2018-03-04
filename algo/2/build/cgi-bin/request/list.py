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
    "status": "bad"
}

isDocHighScore = bool(form.getfirst("isDocHighScore", False))
isHostel = bool(form.getfirst("isHostel", False))
isExternal = bool(form.getfirst("isExternal", False))
isAllHighScore = bool(form.getfirst("isAllHighScore", False))

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
print(json.dumps(response))
