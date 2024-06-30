def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the arguments for the command."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return str(e)
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.lower().strip()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts):
    name, new_number = args
    contacts[name] = new_number
    return "Contact updated"

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]
   
@input_error 
def show_all(args, contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return "No contacts are available."
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)
        
        match command:
            case 'exit' | 'close':
                print('Good bye!')
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change": 
                print(change_contact(args, contacts))
            case "phone": 
                print(show_phone(args, contacts))
            case "all":
                print(show_all(args, contacts))
            case _:
                print("Invalid command")
    
if __name__ == "__main__":
    main()