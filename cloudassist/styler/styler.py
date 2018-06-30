class Styler(object):
    def __init__(self):
        self.ret_str = ''

    def format_appointments(self, appointments):
        self.ret_str = ''
        self._appand_appointment_header(appointments)
        for appointment in appointments:
            self._appand_formated_appointment(appointment)
        return self.ret_str

    def _appand_appointment_header(self, appointments):
        pass

    def _appand_formated_appointment(self, appointment):
        pass
