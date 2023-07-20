import os
import asyncio
from dotenv import load_dotenv
from scanner_service.scanner_service import ScannerService


async def main():
    api_key = os.getenv('API_KEY')
    file_paths = []

    scanner_service = ScannerService(api_key)
    await scanner_service.scan_and_fetch_results(file_paths)

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())
