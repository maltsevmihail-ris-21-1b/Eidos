import serial
import time
import os


class GCodeSender:
    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(3)
        self.send_line("M105")

    def send_line(self, line):
        """Отправляет одну строку G-кода и ожидает ответа 'ok'"""
        clean_line = line.strip()
        if not clean_line or clean_line.startswith(';'):
            return

        print(f"Отправка екструдеру: {clean_line}")
        self.ser.write(f"{clean_line}\n".encode())


        while True:
            response = self.ser.readline().decode('utf-8').strip()
            if response:
                print(f"Ответ: {response}")
                if 'ok' in response.lower():
                    break

    def process_gcode_line(self, line):
        """Разделяет G-код на движения и экструзию."""
        if line.startswith("G0") or line.startswith("G1"):
            # Разделяем команду на части
            parts = line.split()

            robot_cmd = " ".join([p for p in parts if p.startswith(("X", "Y", "Z", "G", "F"))])

            extruder_cmd = " ".join([p for p in parts if p.startswith(("E", "F"))])

            if robot_cmd:
                print(f"Отправка роботу: {robot_cmd}")
                #gcode_line(robot_cmd)

            if extruder_cmd:
                self.send_line("G1 " + extruder_cmd)
        elif line == "G28":
            #M6 - Смена инструмента под номером. Выполняет сценарий автоматической смены
            #инструмента в соответствии с конфигурацией (с калибровкой) и уходит в
            #домашнюю позицию(она настроена в конфигурации интерпретатора).
            #gcode_line("T2 M6")
        elif line.startswith("G92"):
            parts = line.split()

            robot_cmd = " ".join([p for p in parts if p.startswith(("X", "Y", "Z"))])

            extruder_cmd = " ".join([p for p in parts if p.startswith(("E"))])

            if robot_cmd:
                print(f"Отправка роботу: {robot_cmd}")
                #gcode_line(robot_cmd)

            if extruder_cmd:
                self.send_line("G92 " + extruder_cmd)
        else:
            if "M104" in line or "M109" in line or "M105" in line or "M107" in line or "M106" in line:
                self.send_line(line)
            elif "M82" in line or "M83" in line:
                self.send_line(line)
        

    def send_file(self, filename):
        """Отправляет G-код из файла построчно"""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не найден")

        with open(filename, 'r') as f:
            for line in f:
                self.process_gcode_line(line)

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