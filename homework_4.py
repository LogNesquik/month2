class Contact:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.phone_number = phone_number
        self.id = id

    @staticmethod
    def validate_phone_number(phone_number):
        if len(phone_number) == 10:
            return True
        return False
    

class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id += 1
            id = cls.last_id
            contact = Contact(name, phone_number, id)
            cls.all_contacts.append(contact)
            print(f"Контакт {name} добавлен.")
        else:
            raise ValueError("ОШИБОЧКА ВЫШЛА :))")
    @classmethod
    def remove_contact(cls, id):
        for contact in cls.all_contacts:
            if contact.id == id:
                cls.all_contacts.remove(contact)
                print(f"Контакт с ид {id} успешно удален.")
            # raise ValueError("Такой ид не найден в базе...")
            return "error"



# пример использования
print(ContactList.last_id) # 0

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
print(ContactList.last_id) # 2

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone_number, contact.id)
    # Виктор Цой 0500123456 2

