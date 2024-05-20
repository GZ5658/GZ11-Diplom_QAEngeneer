# GZ11-Diplom_QAEngeneer
Работа с базой данных

Задание 1
ТК-1  проверить, отображается ли созданный заказ в базе данных.
Окружение: Яндекс Самокат версия 2.0
Предусловия:
1.	Созданы курьеры с Логинами: Zinur, Tanya И Artem
2.	Создано 9 заказов
3.	Курьер Zinur принял в работу 3 заказа, два из них завершил
4.	Курьер Tanya приняла в работу 2 заказа, ни один не завершила
5.	Курьер Artem принял в работу 2 заказа, один из них завершил
Шаги: 
1.	Подключиться к БД и вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true):
a.	$ ssh-keygen
b.	$ cat ~/.ssh/id_rsa.pub
c.	$ ssh <имя пользователя>@<хост> -p <порт>
d.	psql -U morty -d scooter_rent 
e.	password: smith
f.	SELECT c.login AS "courierLogin",
       COUNT(o.id) AS "countDelivery"
FROM "Couriers" AS c
LEFT JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = TRUE
GROUP BY c.login;
2.	Нажать ВВОД
Ожидаемый результат:
courierLogin | countDelivery
--------------+---------------
Artem        |             1
Tanya        |             2
Zinur        |             1
(3 rows)

Задание 2

ТК-2 проверка корректности статуса заказа в БД
Окружение: Яндекс Самокат версия 2.0
Предусловия:
6.	Созданы курьеры с Логинами: Zinur, Tanya И Artem
7.	Создано 9 заказов (записать номера заказов)
8.  Отменить один из заказов
9.	Курьер Zinur принял в работу 3 заказа, два из них завершил (записать номера принятых и завершенных заказов)
10.	Курьер Tanya приняла в работу 2 заказа, ни один не завершила (записать номера принятых и завершенных заказов)
11.	Курьер Artem принял в работу 2 заказа, один из них завершил (записать номера принятых и завершенных заказов)
Шаги: 
1.	Подключиться к БД и вывести список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true):
a.	$ ssh-keygen
b.	$ cat ~/.ssh/id_rsa.pub
c.	$ ssh <имя пользователя>@<хост> -p <порт>
d.	psql -U morty -d scooter_rent 
e.	password: smith
f.	SELECT track AS "trackNumber",
CASE
WHEN finished = TRUE THEN 2
WHEN cancelled = TRUE THEN -1
WHEN "inDelivery" = TRUE THEN 1
ELSE 0
END AS "statusOrders"
FROM "Orders";
4.	Нажать ВВОД
Ожидаемый результат:
 trackNumber | statusOrders
-------------+--------------
      579566 |           -1
      211772 |            0
      324057 |            1
      782499 |            1
      262299 |            1
       92270 |            1
      467703 |            2
      871156 |            2
      209693 |            2
(9 rows)
где trackNumber - уникальный номер заказа
statusOrders: 2 - заказ завершен, 1 - заказ в доставке, -1 - заказ отмене, 0 - заказ не принят курьером

Автоматизация теста к API
Шаги автотеста:
- Выполнить запрос на создание заказа.
- Сохранить номер трека заказа.
- Выполнить запрос на получения заказа по треку заказа.
- Проверить, что код ответа равен 200.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

Отчёт о тестировании

Функциональное тестирование веб-приложения
Приложение проверено на стенде https://f5621eb8-f112-4b79-b566-e4d0fe29f6fd.serverhub.praktikum-services.ru/. Все известные требования были покрыты чек-листом: https://docs.google.com/spreadsheets/d/1MFduybwvVBWdLlEgUc3wryJsB-wRyuWf7CchBUcpdrw/edit#gid=2010888140 .
Так же составлен чек-лист на верстку только для одного экрана https://docs.google.com/spreadsheets/d/1MFduybwvVBWdLlEgUc3wryJsB-wRyuWf7CchBUcpdrw/edit#gid=1553972666 
Результаты выполнения тестов можно посмотреть здесь https://docs.google.com/spreadsheets/d/1MFduybwvVBWdLlEgUc3wryJsB-wRyuWf7CchBUcpdrw/edit#gid=2010888140 . Из 233 успешно прошло 201, не прошло — 27, пропущено — 5
Список багов, найденных при тестировании, разбит по приоритетам:
1.	Неотложные:
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-8/Pri-klike-na-Zakazat-otkryvaetsya-okno-ne-predusmotrennoe-trebovaniyami 
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-9/Knopka-Dalee-aktivna-pri-pustom-pole-Adres-na-stranice-Dlya-kogo-samokat
c.	https://gz5658.youtrack.cloud/issue/GZ11Dip-6/V-pole-Kogda-privezti-samokat-vozmozhno-vybrat-datu-ranee-zavtrashnego-dnya
d.	https://gz5658.youtrack.cloud/issue/GZ11Dip-32/V-okne-Hotite-oformit-zakaz-knopka-Da-ne-klikabelna 
2.	Критические:
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-1/V-pole-Imya-ne-vvoditsya-stroka-s-defisom
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-4/V-pole-Telefon-nelzya-vvesti-10-simvolov
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-5/V-pole-Telefon-validiruetsya-na-13-simvolah
c.	https://gz5658.youtrack.cloud/issue/GZ11Dip-11/Pri-nekorrektno-zapolnennom-pole-Srok-arendy-oshibka-ne-poyavlyaetsya
d.	https://gz5658.youtrack.cloud/issue/GZ11Dip-10/Pri-nekorrektno-zapolnennom-pole-Kogda-privezti-samokat-oshibka-ne-poyavlyaetsya
3.	Серьезные
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-2/V-pole-Familiya-vozmozhno-vvesti-bolee-15-simvolov
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-3/V-pole-Adres-nelzya-vvesti-50-simvolov
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-7/V-pole-Kogda-privezti-samokat-vozmozhno-vvesti-datu-vruchnuyu
4.	Обычные:
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-12/V-pole-Kommentarii-Vozmozhen-vvod-bolee-24-simvolov-a-tak-zhe-simvolov-krome-russkie-bukvy-cifry-probel-tire-tochka-zapyataya
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-19/Otsutstvoval-zapros-na-kuki-pri-otkrytii-glavnoj-stranicy
5.	Незначительные:
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-13/Nesootvetstvie-verstki-Forma-Dlya-kogo-samokat-pole-Stanciya-metro
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-14/Nesootvetstvie-verstki-Forma-Dlya-kogo-samokat-knopka-Dalshe
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-15/Nesootvetstvie-verstki-Forma-Pro-arendu-pole-Cvet
c.	https://gz5658.youtrack.cloud/issue/GZ11Dip-16/Nesootvetstvie-verstki-Forma-Pro-arendu-pole-Kommentarij
d.	https://gz5658.youtrack.cloud/issue/GZ11Dip-17/Nesootvetstvie-verstki-Forma-Pro-arendu-aktivnye-chek-boksy
e.	https://gz5658.youtrack.cloud/issue/GZ11Dip-18/Nesootvetstvie-verstki-Forma-Pro-arendu-aktivnye-chek-boksy 	

Заключение:


1.	Какой баг показался самым критичным? Ответ: Имеется несколько самых критичных багов, при которых можно сделать заказ без указания адреса и выбрать дату доставки самоката ранее завтрашнего дня:
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-9/Knopka-Dalee-aktivna-pri-pustom-pole-Adres-na-stranice-Dlya-kogo-samokat
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-6/V-pole-Kogda-privezti-samokat-vozmozhno-vybrat-datu-ranee-zavtrashnego-dnya
2.	На твой взгляд, какая самая «хитрая» серая зона есть в требованиях? Ответ: Нет информации, как на долго можно заказать самокат? В Faq описано, что заряда хватит на 8 суток катания во сне и сутки на пролет и зарядка не предоставляется. Так же не понятно, как оформляется возврат самоката. Есть еще один момент, доставка самоката за МКАД, Московская область большая и не понятно по какому критерию указывать станцию метро.


3.	Проверенная тобой функциональность готова к релизу? Почему? Ответ: В связи с большим количеством неотложных и критичных багов, функциональность не готова к релизу. Требуется исправление найденных багов и провести ретест.
Ретест багов в мобильном приложении
Был проверен фикс багов. Из них не исправлено 1, исправлено — 2, проверен - 1 (открыт новый БР)

Список багов можно посмотреть здесь:
•	https://gz5658.youtrack.cloud/issue/GZ11Dip-20/Pri-klike-na-notifikaciyu-prilozhenie-lomaetsya [Открыт повторно]
•	https://gz5658.youtrack.cloud/issue/GZ11Dip-21/Vo-vkladke-Moi-otobrazhayutsya-ne-tolko-moi-zakazy-no-i-vse-prinyatye-zakazy [ПРОВЕРЕНО, баг не воспроизводится, оформлен другой БР GZ11Dip-31 ]
•	https://gz5658.youtrack.cloud/issue/GZ11Dip-22/Pri-filtracii-po-stancii-metro-ostayutsya-vse-zakazy-a-ne-tolko-dlya-vybrannoj-stancii [Исправлено]
•	https://gz5658.youtrack.cloud/issue/GZ11Dip-23/Ne-poyavlyaetsya-skroll-v-bloke-filtracii-po-stanciyam-esli-dobavit-bolshe-vosmi-stancij  [Исправлено]

Регрессионное тестирование мобильного приложения по готовым тест-кейсам 
Результаты выполнения регрессионных тестов можно посмотреть здесь: https://docs.google.com/spreadsheets/d/1XAPgooq5m1wNUWfYi95IXbo81acOQJuYdearH7fIylI/edit#gid=0 
Из 10 успешно прошло - 1  , не прошло — 8. пропущено - 1 [Пропущено, в связи невозможностью выполнить пункт 4 Предусловия]
Список багов, найденных при тестировании, разбит по приоритетам:
1.	Неотложные
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-25/Oshibki-prinyatiya-zakaza-ne-proyavlyaetsya-esli-zakaz-vzyal-drugoj-kurer
b.	https://gz5658.youtrack.cloud/issue/GZ11Dip-24/Oshibka-ne-poyavlyaetsya-pri-prinyatii-zakaza-esli-zakaz-otmenilsya
c.	https://gz5658.youtrack.cloud/issue/GZ11Dip-28/Kartochka-sozdaetsya-bez-obyazatelnyh-parametrov
d.	https://gz5658.youtrack.cloud/issue/GZ11Dip-29/Ne-polnostyu-otobrazhayutsya-dannye-v-kartochke-zakazov 
2.	Критические
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-31/Vo-vkladke-Moi-otobrazhaetsya-DVA-odinakovyh-zakaza-kotoryj-prinyal-kurer-2 
a.	https://gz5658.youtrack.cloud/issue/GZ11Dip-30/Pri-nezapolnennom-pole-Cvet-v-kartochke-ne-zapolnyaetsya-znacheniem-Lyuboj 
3.	Серьезные
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-27/U-vkladki-Moi-net-sinej-tochki-kogda-u-Kurera-net-prinyatyh-zakazov 
4.	Обычные
 .	https://gz5658.youtrack.cloud/issue/GZ11Dip-26/Posle-prinyatiya-zakaza-ego-kartochka-ne-uezzhaet-iz-spiska-Vse-s-animaciej-dvizheniya-vverh 

Заключение:
1.	Какой баг показался самым критичным? Ответ: Самым критичным багом оказался бага на создание заказа без передачи обязательных полей https://gz5658.youtrack.cloud/issue/GZ11Dip-28/Kartochka-sozdaetsya-bez-obyazatelnyh-parametrov 
2.	Такой продукт можно выпускать в релиз? Почему? Ответ: продукт не готов к релизу, требуется исправление найденных багов. Так-же требуется доработка на стороне веб версии, в которой имеются баги на создание Заказа на день ранее завтрашнего и без указания адреса. Курьер, получив такой заказ не сможет корректно его обработать. Есть еще момент, когда в карточке заказа не полностью отображаются данные адреса https://gz5658.youtrack.cloud/issue/GZ11Dip-29/Ne-polnostyu-otobrazhayutsya-dannye-v-kartochke-zakazov 
Выводы о проделанной работе
Как для тебя прошла первая практическая часть проекта? С какими сложностями пришлось столкнуться? Что получилось хорошо, а что не очень? Какие мысли остались? 

