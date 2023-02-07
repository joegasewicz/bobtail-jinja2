# bobtail-jinja2
Bobtail middleware for Jinja2 templating

### Install
```bash
pip install bobtail-jinja2
```

### Usage
```python
from bobtail_jinja2 import BobtailJinja2

app = Bobtail(routes=routes)

app.use(BobtailJinja2(template_dir="templates"))
```
