from mycroft import MycroftSkill, intent_file_handler


class Employees(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('employees.intent')
    def handle_employees(self, message):
        self.speak_dialog('employees')


def create_skill():
    return Employees()

