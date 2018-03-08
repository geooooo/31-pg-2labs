/// Главный файл клиентского кода



import "dart:html";
import "dart:convert" show JSON;
import "ajax.dart" as ajax;
import "templates.dart" as tmp;



void main() {

    // Все действия после загрузки страницы
    window.addEventListener("load", (Event event) {

        addFormEventsListen();
        deleteFormEventsListen();
        listFormEventsListen();

    });

}



/// Наблюдение за событиями на форме добавления
void addFormEventsListen() {

    // Получение элементов формы
    final lastName = document.getElementById("lastNameAdd");
    final city = document.getElementById("cityAdd");
    final isDocHighScore = document.getElementById("isDocHighScoreAdd");
    final isHostel = document.getElementById("isHostelAdd");
    final scoreMath = document.getElementById("scoreMathAdd");
    final scorePhys = document.getElementById("scorePhysAdd");
    final scoreInfo = document.getElementById("scoreInfoAdd");

    // Обработка отравки формы
    document.getElementById("formAdd").addEventListener("submit", (Event event) {

        event.preventDefault();

        // Получение данных из формы
        Map<String, String> data = {
            "lastName": lastName.value,
            "city": city.value,
            "isDocHighScore": isDocHighScore.checked,
            "isHostel": isHostel.checked,
            "scoreMath": scoreMath.selectedOptions[0].value,
            "scorePhys": scorePhys.selectedOptions[0].value,
            "scoreInfo": scoreInfo.selectedOptions[0].value,
        };

        // Выполение ajax запроса
        ajax.request(method: "post", url: "/cgi-bin/request/add.py", data: data,
                     onDone: (String result) {
            // Вывод сообщения об ошибке, если что-то пошло не так
            var answer = JSON.decode(result);
            if (answer["status"] == "bad") {
                window.alert(answer["message"]);
            }
        });

    }, false);

}



/// Наблюдение за событиями на форме удаления
void deleteFormEventsListen() {

    // Получение элементов формы
    final inputIsDelAll = document.getElementById("isDelAllDel");
    final inputStudentNumber = document.getElementById("studentNumberDel");

    // Щелчёк по флажку
    inputIsDelAll.addEventListener("change", (Event event) {
        // Делать недоступным поле ввода номера абитуриента,
        // если флажок установлен
        inputStudentNumber.disabled = inputIsDelAll.checked;
    });

    // Обработка отравки формы
    document.getElementById("formDel").addEventListener("submit", (Event event) {

        event.preventDefault();

        // Получение данных из формы
        Map<String, String> data = {
            "isDelAll": inputIsDelAll.checked,
            "studentNumber": inputStudentNumber.value,
        };

        // Выполение ajax запроса
        ajax.request(method: "post", url: "/cgi-bin/request/delete.py", data: data,
                     onDone: (String result) {
            // Вывод сообщения об ошибке, если что-то пошло не так
            var answer = JSON.decode(result);
            if (answer["status"] == "bad") {
                window.alert(answer["message"]);
            }
        });

    }, false);

}



/// Наблюдение за событиями на форме вывода списка
void listFormEventsListen() {

    // Получение элементов формы
    final inputIsAllHighScore = document.getElementById("isAllHighScoreList");
    final inputIsDocHighScore = document.getElementById("isDocHighScoreList");
    final inputIsExternal = document.getElementById("isExternalList");
    final inputIsHostel = document.getElementById("isHostelList");

    // Обработка отравки формы
    document.getElementById("formList").addEventListener("submit", (Event event) {

        event.preventDefault();

        // Получение данных из формы
        Map<String, String> data = {
            "isAllHighScore": inputIsAllHighScore.checked,
            "isDocHighScore": inputIsDocHighScore.checked,
            "isExternal": inputIsExternal.checked,
            "isHostel": inputIsHostel.checked,
        };

        // Выполение ajax запроса
        ajax.request(method: "post", url: "/cgi-bin/request/list.py", data: data,
                     onDone: (String result) {
            // Вывод сообщения об ошибке, если что-то пошло не так
            var answer = JSON.decode(result);
            if (answer["status"] == "bad") {
                window.alert(answer["message"]);
            }
            // Вывод списка абитуриентов
            renderStudentList(answer["students"]);
        });

    }, false);

}



/// Отрисовка списка абитуриентов [list]
void renderStudentList(dynamic list) {
    final studentList = document.getElementById("studentList");

    // Очистка списка
    studentList.setInnerHtml("");

    // Заполнение списка
    for (var student in list) {
        window.console.log(student);
        studentList.append(
            document.createElement("div")
            ..setInnerHtml(tmp.formatStudentTemplate(student))
        );
    }
}
