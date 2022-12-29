import asyncio
from pyppeteer import launch


browser_args = [
    '--single-process',
    f"--window-size=1920, 1080",
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--no-zygote',
    '--start-maximized',
    '--disable-infobars',
    '--ignore-certificate-errors'
]


async def main(html_path: str, file_name: str):
    browser = await launch(headless=True, args=browser_args)
    page = await browser.newPage()
    await page.setViewport({'width': 600, 'height': 300})
    await page.goto(f'file://{html_path}', {'waitUntil': 'load', 'timeout': 1_000})
    await page.screenshot({'path': f'{file_name}'})
    await browser.close()


def html_to_png(html_path: str, file_name: str) -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.get_event_loop().run_until_complete(main(html_path, file_name))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    html_to_png("html_path", "file_name")
