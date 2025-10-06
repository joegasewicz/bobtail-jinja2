from bobtail import Response as BobtailResponse

from bobtail_jinja2.templating import _Template


class Response(BobtailResponse):
    """
    :class:`Response` Extends the default Bobtail Response to include a Jinja2 template attribute.
    :attr jinja2: Jinja2 template engine instance (set by middleware).
    """
    jinja2: _Template
