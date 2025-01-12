from django.db import models

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField()
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        "auth.User",  # add dependency on settings.AUTH_USER_MODEL
        related_name="snippets",
        on_delete=models.CASCADE,
    )
    highlighted = models.TextField()

    class Meta:
        ordering = ("created",)

    def save(self, *args, **kwargs):  # new
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(str(self.language))
        linenos = "table" if self.linenos else False
        options = {"title": str(self.title)} if self.title else {}
        formatter = HtmlFormatter(
            style=str(self.style), linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)
