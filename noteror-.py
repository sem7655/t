hi = 'привет, это курс по python в telegram, сегодня мы научимся работать с командой print() - кстати то, что ты читаешь, было напечатано через print'
print(hi)
task = 'я дам тебе задание, напиши print("Hello_word") '
print(task)
while True:
    task1 = input()
    if task1 == 'print("Hello_word")' or task1 == 'print("hello_word")' or task1 == "print('Hello_word')" or task1 == "print('hello_word')":
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
print('теперь росмотрим перевеные.')
peremen = 'хочу росказать про переменые/nо них можно много говарить но вот база x = 5 print(x) вывод 5'
print(peremen)
task2 = input('терерь зайди в любой копилятор и по эксперементируй но вот задание дай переменой х = 5 и выведи все это и втавь сюда ')
if task2 == '5':
     print ('круто')
while True:
    print('попробуй еще')
    task2 = input()
    print('круто')
    break
