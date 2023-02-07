"""
Templating
"""
from typing import Dict
from bobtail import Request, Response, Tail
from bobtail.middleware import AbstractMiddleware
from jinja2 import Environment, FileSystemLoader


class _Template:
    """
    Template
    """

    env: Environment

    def __init__(self, template_dir: str):
        """
        :param template_dir:
        """
        file_loader = FileSystemLoader(template_dir)
        self.env = Environment(loader=file_loader)

    def render(self, res: Response, template: str, *, data: Dict = None):
        """
        :param res:
        :param template:
        :param data:
        :return:
        """
        res.set_headers({"Content-Type": "text/html"})
        template = self.env.get_template(template)
        if data is None:
            data = {}
        template_str = template.render(**data)
        res.set_html(template_str)


class BobtailJinja2(AbstractMiddleware):
    """
    BobtailJinja2
    """

    template_dir: str

    def __init__(self, *, template_dir: str = "templates"):
        self.template_dir = template_dir

    def run(self, req: Request, res: Response, tail: Tail) -> None:
        """
        :param req:
        :param res:
        :param tail:
        :return:
        """
        setattr(res, "jinja2", _Template(self.template_dir))
        tail(req, res)
