import re

def generator_numbers(text: str):
    number_pattern = r'\d*\.\d+'
    number = re.findall(number_pattern, text)
    for i in number:
        yield float(i)
    
def sum_profit(text: str):
    return sum(generator_numbers(text))


text = "Загальний дохід працівника складається з декількох частин: 1001.12 як основний дохід, доповнений додатковими надходженнями 28.45 і 424.00 доларів."
total_income = sum_profit(text)
print(f"Загальний дохід: {total_income}")