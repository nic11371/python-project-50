Вычислитель отличий

Данное приложение представляет из себя парсер, сравнивающий два файла популярных форматов между собой и показывающий отличие между ними.

Здесь первый файл является старым файлом, второй файл является новым файлом.

Формат входных файлов:

1. JSON
2. YAML, YML

!Важно. Файлы сравниваются одного формата. Нельзя открывать файл YAML/YML и JSON вместе.

Выходные форматы:

1. stylish -- строка, представляет из себя дерево отличий и содержит следующие служебные символы:
* '+' означает добавление новых данных в файл. Новые данные содержатся во втором файле;
* '-' означает удаление данных. Во втором файле нет данных, которые есть в первом.
* '+, -' обновление данных в файле. Данные сдержащиеся в обеих файлах изменили значение.
Если иземенений значения в данных нет -- выводится одна строка с этими данными.
Если изменений не произошло ни в одних данных -- выводится обычное дерево данных.
2. plain -- строка, представляет из себя обычные строки, в каждой из которых напрямую указывается изменения в файлах. В этом формате показываются только измененные данные.
3. json -- строка фората JSON. В каждом ключе данных указывается тип изменения. О данном формате подробнее можно почитать в Интернете. 

Иструкция по установке

1. Для начала необходимо установить окружение. Посмотреть, как устанавливать окружения для разных систем можно здесь https://ru.hexlet.io/courses/python-setup-environment/lessons/venv/theory_unit
2. Установить poetry. Посмотреть можно здесь https://python-poetry.org/docs/#installing-with-pipx
3. Перейти в директорию python-project-50 и ввести poetry install. Данная команда создаст виртуальное окружение в текущей директории.
4. Далее нужно собрать пакет командой make biuld. !Неоходимо находиться в директории python-project, т.к. в ней есть Makefile. Все make команды будут работать только там.
5. Желательно опубликовать приложение в индексе репозиториев PiCl командой make publish.
6. Для установки приложения из пакетов ввести make package-install. Приложение установлено и готово к использованию.
7. Если в процессе установки возникла ошибка, в которой указана невозможность установки по причине того, что файлы уже существуют в системе, то необходимо ввести make package-reinstall. Команда перезапишет предыдущую установку в системе.

Запуск приложения

1. gendiff 'path/name_file1.json/yaml' 'path/name_file2.json/yaml' -- запуск приложения с указанием абсолютного пути к файлам 
2. При запуске без опций по умолчанию вывод происходит в формате stylish
3. --format, -f -- опции формата. Указываются до путей к файлам.
* stylish -- формат stylish
* plain -- формат plain
* json -- формат json
4. make test-coverage -- запуск тестов для приложения. Тесты должны все пройти и указано успешное завершение. В противном случае необходимо обратится за помощью к системному администратору или к разработчику.

Примеры

gendiff tests/fixtures/file1.json tests/fixtures/file2.json
gendiff tests/fixtures/file1.yaml tests/fixtures/file2.yaml
gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
gendiff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json

Ниже показана видеодемонстрация всех случаев запуска.


### Hexlet tests and linter status:
[![Actions Status](https://github.com/nic11371/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/nic11371/python-project-50/actions)
<a href="https://codeclimate.com/github/nic11371/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/29de4b94184ab620c6d3/maintainability" /></a>
<a href="https://codeclimate.com/github/nic11371/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/29de4b94184ab620c6d3/test_coverage" /></a>
<a href="https://asciinema.org/a/2082j12WMnPasesX6FhDkuuqy" target="_blank"><img src="https://asciinema.org/a/2082j12WMnPasesX6FhDkuuqy.svg" /></a>
<a href="https://asciinema.org/a/674742" target="_blank"><img src="https://asciinema.org/a/674742.svg" /></a>
<a href="https://asciinema.org/a/677649" target="_blank"><img src="https://asciinema.org/a/677649.svg" /></a>
<a href="https://asciinema.org/a/678010" target="_blank"><img src="https://asciinema.org/a/678010.svg" /></a>
<a href="https://asciinema.org/a/678011" target="_blank"><img src="https://asciinema.org/a/678011.svg" /></a>