## Задача 5. Счётчик
### Что нужно сделать
Реализуйте декоратор `counter`, считающий и выводящий количество вызовов декорируемой функции.

Для решения задачи нельзя использовать операторы `global` и `nonlocal` (об этом мы ещё расскажем).
### Что оценивается
- Результат вычислений корректен.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
- Во всех декораторах используется `functools.wraps`.
