hi = 'привет, это курс по python в telegram, сегодня мы научимся работать с командой print() - кстати то, что ты читаешь, было напечатано через print'
print(hi)

task = 'я дам тебе задание, напиши print("Hello_word") '
print(task)

while True:
    task1 = input()
    if task1 == 'print("Hello_word")' or task1 == 'print("hello_word")' or task1 == "print('Hello_word')":
        print('да супер')
        print('ты хочешь продолжить учится да или нет')
        response = input("Хотите продолжить изучение? (Да/Нет): ")
        if response.lower() == "да":
            break
    else:
        print('попробуй еще, обрати внимание на буквы. Если ты написал не так, то код не сработает. Пиши все так, как было сказано выше!')
        print(task)

print("К сожалению, IDE в Telegram не может полноценно понимать ваш код.")
print("Рекомендуем писать код в своем редакторе или использовать онлайн-компилятор.")
print("Вот ссылка, где можно удобно писать код онлайн: https://www.programiz.com/python-programming/online-compiler/")
