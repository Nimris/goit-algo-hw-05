import collections
from pathlib import Path
import sys

#Парсинг рядків файлу логів і збереження іх у словниках
def parse_log_line(line: str) -> dict:
    try:
        list_of_logs = line.split(" ", 3)
        return {
        'date': list_of_logs[0],
        'time': list_of_logs[1],
        'level': list_of_logs[2],
        'message': list_of_logs[3]
        }
    except IndexError:
        print("Incorrect log format")
        return {}

#Зчитування рядків і збереження їх у список
def load_logs(path: str) -> list:
    try:
        with path.open("r", encoding = "UTF-8") as file:
            return [parse_log_line(line.strip()) for line in file if parse_log_line(line.strip())]
    except:
        print("Smth went wrong 0_o")
        return []

#Виведення деталей для логів певного рівня        
def filter_logs_by_level(logs: list, level: str) -> list:
    valid_levels = {"INFO", "ERROR", "WARNING", "DEBUG"}
    if level not in valid_levels:
        print(f"Invalid lavel name: '{level}'")
        return []
    
    print(f"Деталі логів для рівня {level}:")
    dictlist = ([log for log in logs if log["level"] == level])
    for dictionary in dictlist:
        print(f"{dictionary['date']} {dictionary['time']} - {dictionary['message']}")
     
#Підрахунок кількості логів всіх рівней
def count_logs_by_level(logs: list) -> dict:
    return dict(collections.Counter(log["level"] for log in logs if "level" in log))

#Виведення кількості
def display_log_counts(counts: dict):
    try:
        print("Рівень логування | Кількість")
        print("---------------- | ---------")
        print(f"INFO             | {counts["INFO"]}")
        print(f"DEBUG            | {counts["DEBUG"]}")
        print(f"ERROR            | {counts["ERROR"]}")
        print(f"WARNING          | {counts["WARNING"]}")
        print("----------------------------")
    except KeyError as e:
        print(f"Key Error: {e}")
    
#Перевірка вводу із консолі
def main():    
    if len(sys.argv) == 2:
        file_path = Path(sys.argv[1])
        lvl = None
    elif len(sys.argv) == 3:
        file_path = Path(sys.argv[1])
        lvl = sys.argv[2].upper()
    else:
        print("Error. Please enter 'python HW3.py <path_to_directory> <log_level>'")
        sys.exit(1)
        
    if not file_path.exists():
        print(f"Error: The path '{file_path}' does not exist.")
        sys.exit(1)    
    
    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if lvl:
        filter_logs_by_level(logs, lvl)
        
        
if __name__ == "__main__":
    main()