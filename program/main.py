import serial
import time
import os


class GCodeSender:
    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)

    def send_line(self, line):
        """Отправляет одну строку G-кода и ожидает ответа 'ok'"""
        clean_line = line.strip()
        if not clean_line or clean_line.startswith(';'):
            return

        print(f"Отправка: {clean_line}")
        self.ser.write(f"{clean_line}\n".encode())


        while True:
            response = self.ser.readline().decode('utf-8').strip()
            if response:
                print(f"Ответ: {response}")
                if 'ok' in response.lower():
                    break
                if 'error' in response.lower():
                    raise Exception(f"Ошибка выполнения: {response}")

    def send_file(self, filename):
        """Отправляет G-код из файла построчно"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не найден")

        with open(filename, 'r') as f:
            for line in f:
                self.send_line(line)

    def close(self):
        self.ser.close()



if __name__ == "__main__":
    PORT = 'COM5'
    GCODE_FILE = 'test.gcode'

    sender = GCodeSender(PORT)
    try:
        print(f"Отправка файла {GCODE_FILE}...")
        sender.send_file(GCODE_FILE)
        print("Отправка завершена успешно!")
    except Exception as e:
        print(f"Ошибка: {str(e)}")
    finally:
        sender.close()