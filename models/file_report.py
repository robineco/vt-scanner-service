class FileReport:
    def __init__(self, json_data):
        self._data = json_data

    @property
    def type_description(self):
        return self._data['attributes']['type_description']

    @property
    def tlsh(self):
        return self._data['attributes']['tlsh']

    @property
    def vhash(self):
        return self._data['attributes']['vhash']

    @property
    def type_tags(self):
        return self._data['attributes']['type_tags']

    @property
    def creation_date(self):
        return self._data['attributes']['creation_date']

    @property
    def last_modification_date(self):
        return self._data['attributes']['last_modification_date']

    @property
    def type_tag(self):
        return self._data['attributes']['type_tag']

    @property
    def times_submitted(self):
        return self._data['attributes']['times_submitted']

    @property
    def total_votes(self):
        return self._data['attributes']['total_votes']

    @property
    def size(self):
        return self._data['attributes']['size']

    @property
    def type_extension(self):
        return self._data['attributes']['type_extension']

    @property
    def last_submission_date(self):
        return self._data['attributes']['last_submission_date']

    @property
    def sandbox_verdicts(self):
        return self._data['attributes']['sandbox_verdicts']

    @property
    def sha256(self):
        return self._data['attributes']['sha256']

    @property
    def tags(self):
        return self._data['attributes']['tags']

    @property
    def last_analysis_date(self):
        return self._data['attributes']['last_analysis_date']

    @property
    def unique_sources(self):
        return self._data['attributes']['unique_sources']

    @property
    def first_submission_date(self):
        return self._data['attributes']['first_submission_date']

    @property
    def ssdeep(self):
        return self._data['attributes']['ssdeep']

    @property
    def md5(self):
        return self._data['attributes']['md5']

    @property
    def sha1(self):
        return self._data['attributes']['sha1']

    @property
    def magic(self):
        return self._data['attributes']['magic']

    @property
    def last_analysis_stats(self):
        return self._data['attributes']['last_analysis_stats']

    @property
    def last_analysis_results(self):
        return self._data['attributes']['last_analysis_results']

    @property
    def reputation(self):
        return self._data['attributes']['reputation']

    @property
    def type(self):
        return self._data['type']

    @property
    def names(self):
        return self._data['attributes']['names']

    @property
    def meaningful_name(self):
        return self._data['attributes']['meaningful_name']

    @property
    def id(self):
        return self._data['id']

    @property
    def links(self):
        return self._data['links']
