# Django-codemirror
Django form widget for [CodeMirror](http://codemirror.net/) text editor.

Installation:
------------

    pip install django-codemirror

settings.py:
```python
INSTALLED_APPS = (
    ...
    'codemirror',
    ...
)

# Default config
CODEMIRROR_CONFIG = {
    'lineNumbers': True,
}
```

Usage:
```python
from django import forms
from codemirror.widgets import CodeMirror

class SomeForm(forms.Form):
    text = forms.CharField(widget=CodeMirror(mode='html'))
```
