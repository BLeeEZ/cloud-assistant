class Styler(object):
    def formatAppointments(self, appointments):
        return_text = self._formatHeader(appointments)
        for appointment in appointments:
            return_text = return_text + '\n' + self._formatAppointment(appointment)
        return return_text

    def _formatHeader(self, appointments):
        return ''

    def _formatAppointment(self, appointment):
        return ''