from cloudassist.styler.styler import Styler

class ListingStyler(Styler):
    def __init__(self):
        Styler.__init__(self)

    def _appand_appointment_header(self, appointments):
        if len(appointments) == 0:
            self.ret_str = self.ret_str + 'No appointments\n'
        else:
            self.ret_str = self.ret_str + 'There are {} appointments\n'.format(len(appointments))

    def _appand_formated_appointment(self, appointment):
        self.ret_str = self.ret_str + '{} {} - {} {}: {}'.format(
            appointment.startDate,
            appointment.startTime,
            appointment.endDate,
            appointment.endTime,
            appointment.summary,
        )
