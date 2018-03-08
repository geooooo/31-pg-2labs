#!/usr/bin/env python
"""
    Обработка формы удаления абитуриента
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

isDelAll = form.getfirst("isDelAll").lower() == "true"
if isDelAll:
    univ.delete_all()
    response["status"] = "ok"
else:
    try:
        studentNumber = int(form.getfirst("studentNumber"))
    except TypeError:
        response["message"] = "Номер студента должен быть числом !"
    else:
        try:
            univ.delete_student(studentNumber)
        except UnivException:
            response["message"] = "Студента с указаным номером не существует !"
        else:
            response["status"] = "ok"

univ.close()
print(json.dumps(response, ensure_ascii=False))
