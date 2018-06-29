from cloudassist.styler.styler import Styler

class ListingStyler(Styler):
    def _formatHeader(self, appointments):
        if len(appointments) == 0:
            return 'No appointments'
        else:
            return 'There are {} appointments'.format(len(appointments))

    def _formatAppointment(self, appointment):
        return '{} {} - {} {}: {}'.format(
            appointment.startDate,
            appointment.startTime,
            appointment.endDate,
            appointment.endTime,
            appointment.summary,
        )
