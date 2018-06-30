from cloudassist.styler.styler import Styler

class ReportStyler(Styler):
    def formatAppointments(self, appointments):
        return_text = self._formatHeader(appointments)
        if len(appointments) > 0:
            prev_appointment = appointments[0]
            return_text = return_text + self._add_day_header(prev_appointment.startDateTime)
        for appointment in appointments:
            if prev_appointment.startDate != appointment.startDate:
                return_text = return_text + self._add_day_header(appointment.startDateTime)
            return_text = return_text + '\n' + self._formatAppointment(appointment)
            prev_appointment = appointment
        return return_text

    def _formatHeader(self, appointments):
        return ''

    def _formatAppointment(self, appointment):
        return_text = ''
        return_text = return_text + '\t\t\t{} - {}\t{}\n'.format(
            appointment.startTime,
            appointment.endTime,
            appointment.summary,
        )
        return return_text

    def _add_day_header(self, target_daytime):
        return_text = ''
        return_text = return_text + '                                                       ┌─────────────┐\n'
        return_text = return_text + '  ─────────────────────────────────────────────────────┘  {}  └─────────────────────────────────────────────────────\n'.format(target_daytime.strftime("%a %d.%m"))
        #┤├
        #return_text = return_text + '                                                       └─────────────┘\n'
        return return_text
