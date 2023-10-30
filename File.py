import os

def get_words(path: str= os.path.dirname(__file__) + '\\' + 'words.txt') -> list[str]:
    '''
    Ошибка если не удалось прочитать файл
    :param path: путь файла
    :return: список слов для игры
    '''
    if not check_file(path):
        print('Ошибка!')
    f = open(path, 'r+', encoding='utf-8')
    text = f.readlines()
    words = str(*text).split()
    f.close()
    return words

def write_record(record: int, file: str= os.path.dirname(__file__) + '\\' + 'record.txt') -> None:
    '''
    Ошибка если не удалось прочитать файл
    :param record: рекорд игрока
    :param file: путь к файлу в который записывается рекорд
    :return:
    '''
    if not check_file(file):
        print('Ошибка!')
    f = open(file, 'r+', encoding='utf-8')
    old_record = f.read()
    if record < int(old_record):
        print('Новый рекорд!')
        f.seek(0)
        f.write(str(record))
    f.close()

def check_file(filename: str) -> bool:
    '''

    :param filename: путь к файлу
    :return: есть ли ошибка
    '''
    error = True
    try:
        text = open(filename, 'r', encoding='utf-8')
    except KeyboardInterrupt:
        print('Вы отменили операцию')
    except IOError:
        print('Невозможно прочитать файл')
    except:
        print('Произошла непредвиденная ошибка')
    else:
        error = False

    return not error