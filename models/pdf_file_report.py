from models.file_report import FileReport


class PdfFileReport(FileReport):
    def __init__(self, json_data):
        super().__init__(json_data)

    @property
    def crowdsourced_yara_results(self):
        return self._data['attributes']['crowdsourced_yara_results']

    @property
    def pdf_info(self):
        return self._data['attributes']['pdf_info']
