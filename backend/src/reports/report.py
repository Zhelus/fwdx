import uuid

class Report:
    def __init__(self, report_id: str = None, report_title: str = None, schedule_id: str = None, reagent_id: str = None, pathogen_id: str = None, creation_date: str = None, mismatches: list = None, report_json: dict = None):
        if report_json is not None:
            self.report_id = report_json['report_id']
            self.report_title = report_json['report_title']
            self.schedule_id = report_json['schedule_id']
            self.reagent_id = report_json['reagent_id']
            self.pathogen_id = report_json['pathogen_id']
            self.creation_date = report_json['creation_date']
            self.mismatches = report_json['mismatches']
        else:
            self.report_id = report_id
            self.report_title = report_title
            self.schedule_id = schedule_id
            self.reagent_id = reagent_id
            self.pathogen_id = pathogen_id
            self.creation_date = creation_date
            self.mismatches = mismatches

    def set_report_id(self, new_id):
        self.report_id = new_id

    def get_json(self):
        report_dict = {
            'report_id': self.report_id,
            'report_title': self.report_title,
            'schedule_id': self.schedule_id,
            'reagent_id': self.reagent_id,
            'pathogen_id': self.pathogen_id,
            'run_date': self.creation_date,
            'mismatches': self.mismatches
        }

        return report_dict
