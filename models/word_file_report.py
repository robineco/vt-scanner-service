from models.file_report import FileReport


class WordFileReport(FileReport):
    def __init__(self, json_data):
        super().__init__(json_data)

    @property
    def sigma_analysis_results(self):
        return self._data['attributes']['sigma_analysis_results']

    @property
    def sigma_analysis_summary(self):
        return self._data['attributes']['sigma_analysis_summary']

    @property
    def bundle_info(self):
        return self._data['attributes']['bundle_info']

    @property
    def sigma_analysis_stats(self):
        return self._data['attributes']['sigma_analysis_stats']
