/// Реализация функций для использования AJAX



import "dart:html";



/// Функция-обратного вызова, которая вызывается когда
/// запрос выполнен успешно
typedef void DoneCallback(String result);



/// Выполнение AJAX запроса
/// по указаному [url] используя метод [method] и передавая в запросе
/// при необходимости данные [data]. При успешном выполнении запроса
/// вызывается указанаая функция обратного вызова [onDone], в которую
/// передаётся ответ от сервера
void request({String url, String method = "get", Map<String, String> data = "",
              DoneCallback onDone}) {

    // Формирование тела запроса, содержащего данные
    String body = "";
    for (var key in data.keys) {
        body += "$key=${data[key]}&";
    }
    body = body.substring(0, body.length - 1);

    // Отправка запроса
    var request = new HttpRequest();
    request
        ..open(method, url, async: true)
        ..setRequestHeader("Content-Type", "application/x-www-form-urlencoded")
        ..addEventListener("readystatechange", (Event event) {
            if (request.readyState == HttpRequest.DONE) {
                onDone(request.responseText);
            }
        })
        ..send(body);

}
