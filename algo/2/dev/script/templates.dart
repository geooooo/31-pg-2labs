/// Предоставление шаблонов для отрисовки на клиенте



/// Заполненение шаблона, представляющего информациию
/// об абитуриенте и возвращение его в качестве результата
String formatStudentTemplate(dynamic student) {
    final id = student["id"].toString();
    final city = student["value"]["city"];
    final lastName = student["value"]["lastName"];
    final info = student["value"]["scores"]["info"].toString();
    final phys = student["value"]["scores"]["phys"].toString();
    final math = student["value"]["scores"]["math"].toString();
    final isHostel = student["groups"].contains("isHostel")? "Да" : "Нет";
    final isDocHighScore = student["groups"].contains("isDocHighScore")? "Да" : "Нет";
    final isAllHighScore = student["groups"].contains("isAllHighScore")? "Да" : "Нет";
    final isExternal = student["groups"].contains("isExternal")? "Да" : "Нет";
    return """
    <div class="list__item list student">
        <div class="list__item">
            №:
            <div class="student__number">$id</div>
        </div>
        <div class="list__item">
            Фамилия:
            <div class="student__lastname">$lastName</div>
        </div>
        <div class="list__item">
            Город:
            <div class="student__city">$city</div>
        </div>
        <div class="list__item">
            Результаты экзамена:
            <div class="list">
                <div class="list__item">
                    Математика:
                    <div class="student__scoreMath">$math</div>
                </div>
                <div class="list__item">
                    Физика:
                    <div class="student__scorePhys">$phys</div>
                </div>
                <div class="list__item">
                    Информатика:
                    <div class="student__scoreInfo">$info</div>
                </div>
            </div>
        </div>
        <div class="list__item">
            Аттестат с отличием:
            <div class="student__isDocHighScore">$isDocHighScore</div>
        </div>
        <div class="list__item">
            Все экзамены на "отлично":
            <div class="student__isAllHighScore">$isAllHighScore</div>
        </div>
        <div class="list__item">
            Иногородний:
            <div class="student__isExternal">$isExternal</div>
        </div>
        <div class="list__item">
            Нуждается в общежитии:
            <div class="student__isHostel">$isHostel</div>
        </div>
    </div>
    """;
}
