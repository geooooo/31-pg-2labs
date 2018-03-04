#!/usr/bin/env python
"""
    Обработка формы добавления абитуриента
"""



import cgitb
import cgi
import json

from univ import Univ



cgitb.enable()
print("Content-Type: text/html; charset=UTF-8\n")



univ = Univ()
student = Univ.new_student()
form = cgi.FieldStorage()
response = {
    "status": "bad",
    "message": "Поля формы заполнены не правильно !"
}

student["lastName"] = form.getfirst("lastName", "").strip()
student["city"] = form.getfirst("city", "").strip()
isDocHighScore = bool(form.getfirst("isDocHighScore", False))
isHostel = bool(form.getfirst("isHostel", False))
student["scores"]["math"] = int(form.getfirst("scoreMath"))
student["scores"]["info"] = int(form.getfirst("scoreInfo"))
student["scores"]["phys"] = int(form.getfirst("scorePhys"))

if student["lastName"] and student["city"]:
    if isDocHighScore:
        student["groups"].append("isDocHighScore")
    if isHostel:
        student["groups"].append("isHostel")
    univ.add_student(student)
    response["status"] = "ok"
    response["message"] = ""

univ.close()
print(json.dumps(response))
