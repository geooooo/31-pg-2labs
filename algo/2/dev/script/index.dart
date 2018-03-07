/// Главный файл клиентского кода



import "dart:html";
import "dart:convert" show JSON;
import "ajax.dart" as ajax;



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

    // Обработка отравки формы
    document.getElementById("formAdd").addEventListener("submit", (Event event) {

        event.preventDefault();

        // Получение элементов формы
        final lastName = document.getElementById("lastNameAdd");
        final city = document.getElementById("cityAdd");
        final isDocHighScore = document.getElementById("isDocHighScoreAdd");
        final isHostel = document.getElementById("isHostelAdd");
        final scoreMath = document.getElementById("scoreMathAdd");
        final scorePhys = document.getElementById("scorePhysAdd");
        final scoreInfo = document.getElementById("scoreInfoAdd");

        // Получение данных из формы
        Map<String, String> data = {
            "lastName": lastName.value,
            "city": city.value,
            "isDocHighScore": isDocHighScore.checked,
            "isHostel": isDocHighScore.checked,
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

    final inputIsDelAll = document.getElementById("isDelAllDel");
    final inputStudentNumber = document.getElementById("studentNumberDel");

    inputIsDelAll.addEventListener("change", (Event event) {
        // Делать недоступным поле ввода номера абитуриента,
        // если флажок установлен
        inputStudentNumber.disabled = inputIsDelAll.checked;
    });

    // TODO: ...

}



/// Наблюдение за событиями на форме вывода списка
void listFormEventsListen() {

    // TODO: ...

}

/*
window.addEventListener("load", () => {


// Раздел добавления абитуриента

let submitAdd = document.getElementById("submitAdd");
submitAdd.addEventListener("click", (e) => {
    e.preventDefault();
    let xhr = new XMLHttpRequest();
    xhr.open("post", "cgi-bin/request/add.py", true);
    xhr.addEventListener("readystatechange", () => {
        if (xhr.readyState != 4) {
            return;
        }
        console.log(JSON.parse(xhr.responseText));
    });
    xhr.send();
});


// Раздел удаления абитуриента

let isDelAll = document.getElementById("isDelAllDel");
let studentNumber = document.getElementById("studentNumberDel");

isDelAll.addEventListener("change", () => {
    if (studentNumber.getAttribute("disabled")) {
        studentNumber.removeAttribute("disabled");
    } else {
        studentNumber.setAttribute("disabled", "disabled");
    }
});*/
