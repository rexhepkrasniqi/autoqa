from app.models import Task, Step
from base.settings import MEDIA_ROOT
from playwright.sync_api import sync_playwright
from time import sleep

class Worker:
    def __init__(self, task: Task) -> None:
        self.task = task
        self.steps = Step.objects.filter(task=self.task).all()
        self.page = None

    def run(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            self.page = browser.new_page()
            for step in self.steps:

                try:
                    if str(step.action) == "go_to":
                        self.go_to(step.target)
                    elif str(step.action) == "click":
                        self.click(step.target)
                    elif str(step.action) == "locate":
                        self.locate(step.target)
                    elif str(step.action) == "fill":
                        self.fill(step.target)
                    elif str(step.action) == "breakpoint":
                        sleep(10)
                except Exception as e:
                    browser.close()
                    self.mark_failed_(str(e))
                    step.status = False
                    step.save()
                    self.screenshot()
                    return False

                step.status = True
                step.save()
            self.mark_success_()
            self.screenshot()
            browser.close()
    
    def go_to(self, target):
        self.page.goto(target)
    
    def click(self, target):
        self.page.locator(target).click()
    
    def locate(self, target):
        self.page.locator(target).inner_html()
    
    def fill(self, target):
        """
        expecting target with ' | ' in the middle of
        locator and what to write
        """
        selector = target.split("|")[0]
        content = target.split("|")[1]
        self.page.locator(selector).type(content)
    
    def counter(self):
        """
        expecting target with ' | ' in the middle of
        locator and count condition
        elements = page.locator("div")
        div_counts = elements("(divs, min) => divs.length >= min", 10)
        """
        ...
    
    def hover(self):
        """
        locator.hover(**kwargs)
        """
        ...

    def is_visible(self):
        """
        locator.is_visible(**kwargs)
        """
        ...
    
    def keyboard_type(self):
        """
        element.type("hello") # types instantly
        element.type("world", delay=100) # types slower, like a user
        """
        ...

    def wait_for(self):
        """
        order_sent = page.locator("#order-sent")
        order_sent.wait_for()
        """
        ...
    
    def check_title(self):
        """
        page.title()
        """
        ...
    
    def input_file(self):
        """
        page.set_input_files(selector, files, **kwargs)
        """
        ...
    
    def screenshot(self):
        """
        Screenshot the page
        """
        self.page.screenshot(path=f"{MEDIA_ROOT}screenshot.png")
    
    def wait(self, target):
        "time.sleep()"
        ...
    
    def mark_success_(self):
        self.task.message = "Successfully finished"
        self.task.status = "success"
        self.task.save()

    def mark_failed_(self, message):
        self.task.message = str(message)
        self.task.status = "failed"
        self.task.save()
