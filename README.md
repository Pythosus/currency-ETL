# 📌 Currency-ETL

> Мини-проект для изучения Apache Airflow и построения ETL-пайплайнов. Собирает актуальные курсы валют и криптовалют, сохраняет их в PostgreSQL.

![Статус](https://img.shields.io/badge/status-active-success)

## О проекте
Проект автоматизирует процесс получения финансовых данных:
* Парсит курсы валют с сайта ЦБ РФ
* Получает данные о криптовалютах
* Загружает всё в базу данных PostgreSQL
* Управляется через Apache Airflow

## 🛠 Стек технологий
* Оркестратор - Apache Airflow
* БД - PostgreSQL
* Основные библитеки для Python - psycopg2, request, beatifulsoup, apache-airflow

## 🚀 Запуск проекта локально
Чтобы развернуть проект на вашем компьютере, выполните следующие шаги:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Pythosus/currency-ETL.git
2. **Установите библиотеки:**
   ```bash
   pip install -r requirements.txt
3. **Запустите контейнер**
   ```bash
   docker-compose up -d
4. **Веб-интерфейс оркестратора**
     * URL: http://localhost:8085
     * Login: admin
     * Password: admin
5. **Просмотр результатов в БД**
     * Host: localhost
     * Port: 5433
     * Database: money
     * Password: 1276
