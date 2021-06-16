from contextlib import ContextDecorator

class log_em_arquivo(ContextDecorator):
    def __init__(self,file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode
        self._file = None

    def __enter__(self):
        print(f"Open File {self._file_name}")
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self,exc_type,exc_value,exc_traceback):
        print(f"Close File {self._file_name}")
        self._file.close()

@log_em_arquivo("lucas3.txt","w+" )
def write_to_file():
    print("Nada do acesso foi retornado do método __enter__")


if __name__ == "__main__":
    write_to_file()
    with log_em_arquivo("lucas3.txt","w") as f:
       f.write("TestLucas")