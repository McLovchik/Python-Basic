# теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи;
# на выходе из менеджера подавляются все исключения, связанные с файлами.


class File:
    """
        Модернизированная версия контекст-менеджера File
    """
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File("example.txt", "w") as file:
    file.write("Всем привет!")
