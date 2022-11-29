# для установки magic на винду использовать
# pip install python-magic-bin==0.4.14
# для установки magic на линукс использовать
# pip install python-magic
# https://github.com/ahupp/python-magic
import magic
import os


class WorkWithFile:

    # возвращаяет MIME-type файла
    def get_MIME_file_format(self, file_path):
        mime = magic.Magic(mime=True)
        return mime.from_file(file_path)

    def get_file_name_by_path(self, path):
        return os.path.basename(path)

    # The method getcwd() returns current working directory of a process.
    def get_current_working_directory(self):
        return os.getcwd()






