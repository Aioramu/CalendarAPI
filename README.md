# Запуск
### для запуска используйте docker-compose:
```
docker-compose up
```

Eсли вы не добавили себя в группу пользователей docker -добавьте в начале sudo.

Для ручного запуска тестов необходимо запустить и войти в контейнер,полная последовательность комманд:
```
docker-compose up -d
docker exec -it calendarapi_web_1 bash -c "pytest authorization/tests ; pytest events/tests "
```

Документация: https://app.swaggerhub.com/apis-docs/Aioramu/CalendarAPI/1.0.0#/
