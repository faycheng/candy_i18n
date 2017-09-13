# Candy I18N

A smart internationalization library for Python.

### Installation

Clone this repo to your local machine and move to the repo directory:

```
git clone https://github.com/faycheng/candy_i18n.git
cd candy_i18n
```

Execute setup.py:

```
python setup.py install
```

### Quick Start

First, install alias of translation to builtins:

```
from candy_i18n.i18n import install
install('_')
```

Then, wrap all of the string that will be translated:

```
class PathError(BaseException):
    ERR_MSG = _('Path({}) is invalid')  # wrap exception message

    def __init__(self, path):
        self.message = self.ERR_MSG.format(path)
        super(PathError, self).__init__(self.message)

```

Now, every thing is ok.

### CLI Usage

Supported commands:

```
compile     Compile po to mo file
gen         Extract source code and generate pot file
init        Init locale directory
status      Show metadata, translated entries and untranslated entries
```




