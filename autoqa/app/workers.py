from app.models import Task, Step
from playwright.sync_api import sync_playwright

class Worker:
    def __init__(self, task: Task) -> None:
        self.task = task
        self.steps = Step.objects.filter(task=self.task).all()

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()

            for step in self.steps:
                if str(step.action) == "go_to":
                    self.go_to(page, step.target)
                elif str(step.action) == "click":
                    self.click(page, step.target)
                elif str(step.action) == "locate":
                    self.locate(page, step.target)
                elif str(step.action) == "fill":
                    self.fill(page, step.target)
            browser.close()
    
    def go_to(self, page, target):
        page.goto(target)
    
    def click(self, page, target):
        page.locator(target).click()
    
    def locate(self, page, target):
        page.locator(target).inner_html()
    
    def fill(self, page, target):
        target = target.split("|")[0]
        content = target.split("|")[1]
        page.locator('#area').type(content)
