import asyncio

async def fast_operation(a, b):
    result = a + b
    print("Быстрый результат операции:", result)

async def slow_operation(a):
    await asyncio.sleep(a**2)
    print("Медленная операция завершена")

async def main():
    task1 = asyncio.create_task(fast_operation(4, 4))
    task2 = asyncio.create_task(slow_operation(2))

    await asyncio.gather(task1, task2)

asyncio.run(main())
import asyncio

async def answer_phone_call():
    print("Ответ на телефонный звонок")
    await asyncio.sleep(3)
    print("Телефонный звонок завершен")

async def welcome_visitors():
    print("Приветствуем посетителей")
    await asyncio.sleep(2)
    print("Взаимодействие с посетителем завершено")

async def book_flight_tickets():
    print("Бронирование авиабилетов")
    await asyncio.sleep(5)
    print("Бронирование авиабилета завершено")

async def control_meeting_schedules():
    print("Контроль расписания встреч")
    await asyncio.sleep(4)
    print("Контроль расписания встреч завершен")

async def fill_documents():
    print("Оформление документов")
    await asyncio.sleep(1)
    print("Заполнение документов завершено")

async def secretary_workflow():
    tasks = [
        answer_phone_call(),
        welcome_visitors(),
        book_flight_tickets(),
        control_meeting_schedules(),
        fill_documents()
    ]

    await asyncio.gather(*tasks)

asyncio.run(secretary_workflow())
