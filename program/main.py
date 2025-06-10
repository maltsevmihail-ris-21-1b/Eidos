import serial
import time
import os


class GCodeSender:
    float currentFRate = None

    def __init__(self, port, baudrate=115200):
        self.ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(3)
        self.send_line("M105") #получение информационных соообщений при первом подключении к плате

    def send_line(self, line):
        clean_line = line.strip()
        if not clean_line or clean_line.startswith(';'):
            return

        #print(f"Отправка екструдеру: {clean_line}")
        self.ser.write(f"{clean_line}\n".encode())

        while True:
            response = self.ser.().decodreadlinee('utf-8').strip()
            if response:
                #print(f"Ответ: {response}")
                if 'ok' in response.lower():
                    break

    def parse_gcode(gcode):
        x = y = z = f = e = None
        
        parts = gcode.split()
        
        for part in parts:
            if part.startswith('X'):
                x = float(part[1:])
            elif part.startswith('Y'):
                y = float(part[1:])
            elif part.startswith('Z'):
                z = float(part[1:])
            elif part.startswith('F'):
                f = float(part[1:])
            elif part.startswith('E'):
                e = float(part[1:])
        return x, y, z, f, e

    def process_gcode_line(self, line):
        if line.startswith("G0") or line.startswith("G1"):
            x, y, z, f, e = parse_gcode(line)
            point = matrix4()
            if x is not None:
                point.x = x
            if y is not None:
                point.y = y
            if z is not None:
                point.z = z
            if f is not None:
                self.currentFRate = f
            if e is not None:
                self.send_line("G1 E" + str(e) + " F" + str(currentFRate))

            if x is not None or y is not None or z is not None:
                print(f"Отправка роботу: {robot_cmd}")
                #параметры     точка   система ккорд скорость в mm/sec  ускорение  сглаживание инструмент
                line_with_base(point, "printerbed2", currentFRate * 60, 0.0,       0.0,        "extruder")

        elif line == "G28":
            #переход в домашнюю позицию(начало координат)
            point = matrix4()
            point.x = 0
            point.y = 0
            point.z = 0
            
            #параметры     точка   система ккорд скорость в mm/sec  ускорение  сглаживание инструмент
            line_with_base(point, "printerbed2", currentFRate * 60, 0.0,       0.0,        "extruder")
        elif line.startswith("G92"):
            #задание новой позиции
            #подразумевается использование только с параметром E
            x, y, z, e = parse_gcode(line)
            
            if e is not None:
            self.send_line("G92 E" + str(e))
        else:
            if "M104" in line or "M109" in line or "M105" in line or "M107" in line or "M106" in line:
                self.send_line(line)
            elif "M82" in line or "M83" in line:
                self.send_line(line)
    
    def send_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Файл {filename} не найден")

        with open(filename, 'r') as f:
            for line in f:
                self.process_gcode_line(line)

    def close(self):
        self.ser.close()

if __name__ == "__main__":
    PORT = 'COM5' #номер com порта
    GCODE_FILE = 'test.gcode' #файл с g-code команадми

    sender = GCodeSender(PORT)
    sender.send_file(GCODE_FILE)
    sender.close()