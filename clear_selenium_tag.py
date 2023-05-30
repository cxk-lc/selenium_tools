from selenium import webdriver


class CreateChromeDriver(object):

    def __init__(self, headless):
        self.web_ops = webdriver.ChromeOptions()

        if headless:
            self.web_ops.add_argument('--headless')

        # 去掉受到自动软件控制提示
        self.web_ops.add_experimental_option('excludeSwitches',
                                             ['enable-automation'])
        self.web_ops.add_experimental_option('useAutomationExtension', False)

    def create_chrome_driver_new(self, headless=False):
        # chrome ver 88+

        self.web_ops.add_argument(
            '--disable-blink-features=AutomationControlled')
        web_browser = webdriver.Chrome(options=self.web_ops)

        return web_browser

    def create_chrome_driver_old(self, headless=False):
        # chrome ver 88-
        self.web_ops = webdriver.ChromeOptions()
        if headless:
            self.web_ops.add_argument('--headless')

        web_browser = webdriver.Chrome(options=self.web_ops)

        # 修改navigator.webdriver为undefined
        web_browser.execute_cdp_cmd(
            'Page.addScriptToEvaluateOnNewDocument',
            {
                'source': """
            navigator.webdriver = undefined
            Object.defineProperty(navigator, "webdriver", {get: () => undefined})
            """
            })
        return web_browser
