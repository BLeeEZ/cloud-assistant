from cloudassist.styler.styler import Styler

class ReportStyler(Styler):
    def __init__(self):
        Styler.__init__(self)

    def format_appointments(self, appointments):
        self.ret_str = ''
        self._appand_appointment_header(appointments)
        if len(appointments) > 0:
            prev_appointment = appointments[0]
            self._appand_day_header(prev_appointment.startDateTime)
        for appointment in appointments:
            if prev_appointment.startDate != appointment.startDate:
                self._appand_day_header(appointment.startDateTime)
            self._appand_formated_appointment(appointment)
            prev_appointment = appointment
        return self.ret_str

    def _appand_formated_appointment(self, appointment):
        self.ret_str = self.ret_str + '\t\t\t{} - {}\t{}\n'.format(
            appointment.startTime,
            appointment.endTime,
            appointment.summary,
        )

    def _appand_day_header(self, target_daytime):
        self.ret_str = self.ret_str + '                                                       ┌─────────────┐\n'
        self.ret_str = self.ret_str + '  ─────────────────────────────────────────────────────┘  {}  └─────────────────────────────────────────────────────\n'.format(target_daytime.strftime("%a %d.%m"))
        #┤├
        #self.ret_str = self.ret_str + '                                                       └─────────────┘\n'
