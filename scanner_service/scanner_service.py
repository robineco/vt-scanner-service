import aiohttp
import asyncio
import logging

from models.file_report import FileReport
from models.word_file_report import WordFileReport
from util.response_parser import parse_analysis_results

logging.basicConfig(
    # filename="scanner_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class ScannerService:
    def __init__(self, api_key):
        self.headers = {
            "accept": "application/json",
            "x-apikey": api_key,
        }
        self.logger = logging.getLogger("ScannerService")

    async def make_api_call_async(self, url, method, files=None):
        async with aiohttp.ClientSession() as session:
            if method == 'GET':
                async with session.get(url, headers=self.headers) as response:
                    return await response.json()
            elif method == 'POST':
                async with session.post(url, data=files, headers=self.headers) as response:
                    return await response.json()

    async def fetch_analysis_results_async(self, analysis_id):
        url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
        self.logger.info(f"Fetching analysis results for ID: {analysis_id}")
        return await self.make_api_call_async(url, 'GET')

    async def analyze_file_async(self, file_path):
        url = "https://www.virustotal.com/api/v3/files"
        files = {"file": open(file_path, "rb")}
        self.logger.info(f"Uploading file for analysis: {file_path}")
        return await self.make_api_call_async(url, 'POST', files=files)

    async def fetch_file_report(self, sha256):
        url = f"https://www.virustotal.com/api/v3/files/{sha256}"
        return await self.make_api_call_async(url, 'GET')

    async def analyze_files_async(self, file_paths):
        tasks = [self.analyze_file_async(file_path) for file_path in file_paths]
        return await asyncio.gather(*tasks)

    async def scan_and_fetch_results(self, file_paths):
        results = await self.analyze_files_async(file_paths)

        for idx, result in enumerate(results, start=1):
            analysis_id = result['data']['id']
            self.logger.info(f"Fetching analysis result for file {idx} (ID: {analysis_id})...")
            analysis_result = await self.fetch_analysis_results_async(analysis_id)
            parsed_result = await parse_analysis_results(analysis_result)
            #self.logger.info(parsed_result)
            hash = parsed_result['sha256']
            file_report = await self.fetch_file_report(hash)
            self.logger.info(file_report['data'])
            report = WordFileReport(file_report['data'])
            self.logger.info(report.type_description)
            self.logger.info(report.bundle_info)
