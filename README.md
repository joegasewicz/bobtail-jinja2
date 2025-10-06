# bobtail-jinja2
Bobtail middleware for Jinja2 templating

### Install
```bash
pip install bobtail-jinja2
```

### Usage
```python
from bobtail_jinja2 import BobtailJinja2, Response

app = Bobtail(routes=routes)

app.use(BobtailJinja2(template_dir="templates"))
```

Render the template in a Bobtail handler. BobtailJinja2 provides a Bobtail handler
`Response` type that also include the Jinja2 template attribute for IntelliSense etc.
```python
from bobtail import AbstractRoute, Request
from bobtail_jinja2 import BobtailJinja2, Response
class HomeRoute(AbstractRoute):

    def get(self, req: Request, res: Response) -> None:
        res.set_headers({
            "Content-Type": "text/plain",
        })
        res.jinja2.render(res, "routes/home.jinja2", data={"title": "Welcome to Lanka Note"})
```
