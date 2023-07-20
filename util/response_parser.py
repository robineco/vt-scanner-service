async def parse_analysis_results(response):
    meta = response['meta']
    file_info = meta['file_info']
    data = response['data']
    attributes = data['attributes']
    stats = attributes['stats']

    analysis_info = {
        'sha256': file_info['sha256'],
        'sha1': file_info['sha1'],
        'md5': file_info['md5'],
        'file_size': file_info['size'],
        'status': attributes['status'],
        'harmless_count': stats['harmless'],
        'type_unsupported_count': stats['type-unsupported'],
        'suspicious_count': stats['suspicious'],
        'confirmed_timeout_count': stats['confirmed-timeout'],
        'timeout_count': stats['timeout'],
        'failure_count': stats['failure'],
        'malicious_count': stats['malicious'],
        'undetected_count': stats['undetected'],
    }
    return analysis_info
