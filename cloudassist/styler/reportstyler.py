from cloudassist.styler.styler import Styler

class ReportStyler(Styler):
    def _formatHeader(self, appointments):
        return ''

    def _formatAppointment(self, appointment):
        return_text = ''
        return_text = return_text + '                                                       ┌─────────────┐\n'
        return_text = return_text + '  ─────────────────────────────────────────────────────┤  {}  ├─────────────────────────────────────────────────────\n'.format(appointment.startDateTime.strftime("%a %d.%m"))
        return_text = return_text + '                                                       └─────────────┘\n'
        return_text = return_text + '\t\t\t{} - {}\t{}\n'.format(
            appointment.startTime,
            appointment.endTime,
            appointment.summary,
        )
        return return_text
