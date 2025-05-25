**УДК 004.4,  67.02, 621.9.06**
<p align="center";"><strong>Мальцев М. Ю., Курушин Д. С.</strong></p>

<p align="center";"><strong>РАЗРАБОТКА ПРОГРАММНОГО И АППАРАТНОГО ОБЕСПЕЧЕНИЯ СОПРЯЖЕНИЯ ГОЛОВКА-РОБОТ ДЛЯ УСТАНОВКИ ТЕРМОЭКСТРУЗИОННОЙ ПЕЧАТИ С ПОМОЩЬЮ РОБОТА-МАНИПУЛЯТОРА EIDOS</strong></p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;В статье рассматривается разработка программного и аппаратного обеспечения для интеграции термоэкструзионной печати с промышленным роботом-манипулятором Eidos. Предложенное решение позволяет использовать робот в качестве 3D-принтера, обеспечивая большую гибкость и расширенную рабочую зону по сравнению с традиционными декартовыми системами. Для реализации проекта использовались современные инструменты и технологии, включая язык программирования Python, термоэкструдер, плата микроконтроллера, а также сам робот-манипулятор.</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;<strong>Ключевые слова:</strong> аддитивное производство; 3D-печать; робот-манипулятор; термоэкструзионная печать; G-код; микроконтроллер; программно-аппаратный комплекс.</p>

<p align="center";"><strong>Maltsev M. Y., Kurushin D. S.</strong></p>

<p align="center";"><strong>DEVELOPMENT OF SOFTWARE AND HARDWARE FOR INTERFACE BETWEEN HEAD AND ROBOT FOR INSTALLING THERMAL EXTRUSION PRINTING USING THE EIDOS ROBOT-MANIPULATOR</strong></p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;This article discusses the development of software and hardware for integrating thermal extrusion printing with the Eidos industrial robotic arm. The proposed solution allows the robot to be used as a 3D printer, providing greater flexibility and an expanded work area compared to traditional Cartesian systems. To implement the project, modern tools and technologies were used, including the Python programming language, a thermal extruder, a microcontroller board, and the robotic manipulator itself.</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;<strong>Keywords:</strong> additive manufacturing; 3D printing; robotic manipulator; thermal extrusion printing; G-code; microcontroller; hardware and software system.</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Современные технологии аддитивного производства открывают новые перспективы в промышленности и робототехнике. Интеграция методов 3D-печати с роботизированными системами позволяет создавать сложные конструкции с высокой точностью. Особый интерес представляет использование промышленных роботов-манипуляторов для аддитивного производства, что существенно расширяет возможности по сравнению с традиционными 3D-принтерами.</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Робот-манипулятор Eidos A12(рисунок 1), разработанный российской компанией «Эйдос Робототехника», представляет собой перспективную платформу для реализации подобных решений. Его шестиосевая конструкция и открытая система управления на базе Python делают его идеальным кандидатом для интеграции с технологиями 3D-печати.</p>


<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Данная робототехническая система состоит из следующих компонентов.</p>
-	Робот-манипулятор. 
-	Шкаф управления роботом. 
-	Пульт управления RCS HMI. 
-	Соединительные кабели. 
-	Программное обеспечение.

<div align="center";><img src="https://optim.tildacdn.com/tild6435-3966-4835-b833-386231663430/-/resize/744x/-/format/webp/004_copy_3.png.webp"></div>
<p align="center";">Рисунок 1 – Робот-манипулятор Eidos A12[1]</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Для реализации проекта должны быть выполнены следующие программно-аппаратные решения:</p>

1. Установка термоэкструдера на фланец робота-манипулятора при помощи соответствующего переходника.
2. Установка управляющего микроконтроллера и проводов на манипулятора без ограничения его возможностей передвижения.
3. Разработка программы, связывающей плату микроконтроллера и программу на компьютере робота для совместной работы.

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Устройство термоэкструдера приведено на рисунке 2. На рисунке стрелками обозначены основные элементы термоэкструдера для 3D-принтера.</p>

<div align="center";><img src="https://robot-on.ru/images/articles/desc/3dprinter-09.jpg"></div>
<p align="center";">Рисунок 2 – Устройство термоэкуструдера[2]</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Процесс печати модели на любом 3D принтере происходит под управлением специальных G- и M-команд. G- и M-команды – это язык программирования для станков с числовым программным управлением. Пример кода G-команды пердставлен на листинге 1.</p>
Листинг 1 – Пример G-код команды(Ускоренное перемещение инструмента)

G0 X0 Y0 Z100

&nbsp;&nbsp;&nbsp;&nbsp;Здесь G0 – номер команды; X0, Y0, Z100 – координаты перемещения.
<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Робот-манипулятор представляет собой устройство управления головкой экструдера, поэтому команды, отвечающие за движение головкой, выполняются на компьютере робота, а команды, реализующие процесс печати, посылаются на плату микроконтроллера. Плата получает команды от компьютера робота, выполняет их и обеспечивает обратную связь.</p>
<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Программное обеспечение робота включает в себя встроенный интерпретатор G-команд, а также свой программный редактор в пульте управления RCS HMI[3]. Плата микроконтроллера прошита специальной прошивкой для 3D-принтеров, прошивка позволяет принимать G-команды по USB соединению, выполнять их и предоставлять обратную связь компьютеру робота.
На листинге 2 представлен пример кода отправки команды на плату и получения обратной связи.
</p>
&nbsp;&nbsp;&nbsp;&nbsp;Листинг 2 – Код отправки команды на плату

```python
import serial
import time
port = "COM3" 
baudrate = 115200 
ser = serial.Serial(port, baudrate, timeout=1)
time.sleep(2) 
def send_gcode(command):
    print(f"Отправка: {command}")
    ser.write((command + "\n").encode())
    while True:
        response = ser.readline().decode().strip()  
        if not response:
            continue 
        print(f"Ответ: {response}")
        if response == "ok":
            break
        elif "error" in response.lower(): 
            raise Exception(f"Ошибка платы: {response}")
```

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;Разработанный программно-аппаратный комплекс позволяет эффективно использовать робот-манипулятор Eidos для задач 3D-печати. К преимуществам решения можно отнести следующее: значительное расширение рабочей области по сравнению с традиционными 3D-принтерами, использование существующего оборудования без значительных доработок. Также открыты перспективы для дальнейшей доработки проекта, включая оптимизацию алгоритмов генерации G-кода для шести осевой системы робота и управление экструдером по сети WI-Fi.</p>

<p align="center";"><strong>Библиографический список</strong></p>

1. Промышленный робот манипулятор А12-1450 - https://prorobotov.org/marketplace_robotov/promyshlennye_roboty/995/
2. Изучение особенностей 3D-принтера - https://robot-on.ru/articles/izuchenie-osobennostey-3d-printera
3. OOO «Эйдос-Робототехника» «Руководство пользователя RCS Core, RCS HMI Версия 3.3», 2024. — 368 с.

<p align="center";"><strong>Сведения об авторах </strong></p>
<p align="justify";">&nbsp;&nbsp;<strong>Курушин Даниил Сергеевич</strong> – кандидат технических наук, доцент кафедры «Информационные технологии и автоматизированные системы», Пермский национальный исследовательский политехнический университет, г. Пермь, e-mail: daniel@kurushin-peram.ru.</p>

<p align="justify";">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<strong>Мальцев Михаил Юрьевич</strong> – cтудент группы РИС-21-1б, Пермский национальный исследовательский политехнический университет, г. Пермь, e-mail: maltsev03@list.ru.</p>
