## Проект Mobile автотестов для приложения Wikipedia

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo_stacks/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo_stacks/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Appium" src="images/logo_stacks/appium.png"></code>
  <code><img width="5%" title="Browserstack" src="images/logo_stacks/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo_stacks/tg.png"></code>
</p>

<!-- Тест кейсы -->

### Что проверяют тесты
1. test search successfully
2. test open article
3. test open article categories
4. test login with invalid data
5. test login successfully

##### Видео прохождение теста на эмуляторе
![This is an image](images/screenshots/test-emulator-demonstration.gif)

##### Видео прохождение теста в Browserstack
![This is an image](images/screenshots/tests_mobile.gif)



<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="images/logo_stacks/jenkins.png">  Запуск проекта в Jenkins
### [Job](https://jenkins.autotests.cloud/job/kudaev-wikipedia-mobile/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение на сервере jenkins.
![This is an image](images/screenshots/jenkins.png)

Также мы можем посмотреть выполнение тестов в консоли перейдя во вкладку "Вывод консоли" у определенного билда
![This is an image](images/screenshots/jenkins_console.png)


<!-- Browserstack -->

### <img width="3%" title="Browserstack" src="images/logo_stacks/browserstack.png"> Запуск проекта в [Browserstack](https://app-automate.browserstack.com/dashboard/v2/builds/be982c566cce4ce727bba8deb0155db9b6cdbcb2/sessions/456557888aad153346a3d5cfb8d1ee56f4d3b642)
##### После запуска сборки в Jenkins, тесты начинают проходить удаленно через Browserstack. Где в реальном времени можно следить за прохождением теста через логи.

![This is an image](images/screenshots/browserstack.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="images/logo_stacks/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](images/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](images/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](images/screenshots/allure_suites.png)

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="images/logo_stacks/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/2027/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](images/screenshots/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](images/screenshots/allure_testops_suites.png)

Во вкладке Launches мы можем видить тестовые прогоны:
![This is an image](images/screenshots/allure_testops_launches.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="images/logo_stacks/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="images/logo_stacks/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](images/screenshots/tg_bot.png)
