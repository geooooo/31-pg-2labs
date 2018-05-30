import 'dart:html';


const List<String> digit_templates = const [
  // 0
  '+++'
  '+*+'
  '+*+'
  '+*+'
  '+++',

  // 1
  '**+'
  '*++'
  '+*+'
  '**+'
  '**+',

  // 2
  '+++'
  '**+'
  '*+*'
  '+**'
  '+++',

  // 3
  '+++'
  '*+*'
  '+++'
  '*+*'
  '+**',

  // 4
  '+*+'
  '+*+'
  '+++'
  '**+'
  '**+',

  // 5
  '+++'
  '+**'
  '+++'
  '**+'
  '+++',

  // 6
  '**+'
  '*+*'
  '+++'
  '+*+'
  '+++',

  // 7
  '+++'
  '*+*'
  '+**'
  '+**'
  '+**',

  // 8
  '+++'
  '+*+'
  '+++'
  '+*+'
  '+++',

  // 9
  '+++'
  '+*+'
  '+++'
  '*+*'
  '+**',
];

const int DELTA = 2;


void main(List<String> args) {

  window.console.clear(null);

  window.addEventListener('load', (e) {

    final HtmlElement field = document.getElementsByClassName('field')[0];
    field.addEventListener('click', (e) {
      final HtmlElement cell = e.target;
      if (cell.classes.contains('field__cell_empty')) {
        cell.classes.remove('field__cell_empty');
        cell.classes.add('field__cell_marked');
        // Проверка совпадения шаблона
        final String cells = field.getElementsByClassName('field__cell')
                                  .map((HtmlElement e) => e.classes.contains('field__cell_empty')? '*' : '+')
                                  .join();
        check(cells);
      } else {
        cell.classes.remove('field__cell_marked');
        cell.classes.add('field__cell_empty');
      }
    });

    final HtmlElement clearConsole = document.getElementsByClassName('clearConsole')[0];
    clearConsole.addEventListener('click', (e) => window.console.clear(null));
  });

}


void check(String cells) {
  for (var dig = 0; dig < digit_templates.length; dig++) {
    var diffCount = 0;
    for (var j = 0; j < 15; j++) {
      if (cells[j] != digit_templates[dig][j]) {
        diffCount++;
      }
    }
    if (diffCount == 0) {
      window.alert('Совпало полностью c цифрой: ${dig}');
      return;
    }
    if (diffCount <= DELTA) {
      print('Совпало частично c цифрой: ${dig} (разница: ${diffCount})');
    }
  }
}
