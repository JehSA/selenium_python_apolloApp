# apollo-selenium.py

<center>

![img](./img/apollo_selenium.jpg)

</center>




---------------------------------------------

[Next Features](#next-features) [Installation](#installation) | [Getting Started](#getting-started) | [Structure](#structure)  | [References](#references)

---------------------------------------------



## Next Features

- [ ] Create Structure of Project(readme)
- [ ] Create GetStarting
- [ ] Create References
- [ ] Create functions to ext.base_page
- [ ] Create docstring
- [ ] Implements dotenv
- [ ] Implements pylint
- [ ] Implements CI/CD
- [ ] Automate Tests with Docker
- [ ] Integrate QA app and Automate Tests

## Installation
You need in your setup:
- 🐍python 
- 📦virtualEnv
- 🖥️Windows (selenium is less problematic)
- 🍫 chocolatey
- 🧑‍💻 Google-Chrome and Firefox

```windows power shell
#windows power shell in admin
# install choco
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# install selenium
choco install selenium-all-drivers

```

## Structure
TODO~~~~~~~~
- .gitignore
- Makefile  
- requirements-dev.txt 
- requirements.txt 
- setup.py 
- middlewareHermes
```
    ├── ext
    │   ├── business 
    │   │   ├── init.py
    │   │   └── payload_client.py   
    │   ├── db
    │   │   ├── init.py
    |   |   └── model.py
    │   ├── model
    |   |   ├── init.py
    │   │   └── ModelClient.py
    │   ├── scheduler
    │   │   └── init.py
    │   │
    │   └── init.py
    |
    ├── .env
    └── app.py
```

|  folder | describe  |
|---|---|
| business | module containing auxiliar job functions |
| db | module that contains the interaction with the database |
| model | module that contains database classes or application classes |
| scheduler | module that contains the call of the scheduler functions |
| config | module that contains the variables configuration |
| app.py | initial application file |
| .env | environment variables configuration file |

ext:
- actions/payload_client -> Receives the payload_client mapped from the ModelClient class.
- db -> Schema to DataBase.
- model -> Consumes claorty payload, maps the fields and returns to payload_client.
- scheduler -> not implemented.

TODO~~~~~~~~
---


## Getting Started
- use virtualenv:
```bash
#windows
virtualenv .env
.env/Scripts/activate
```
```If it doesn't work, try...
python -m venv <enviroment-name>
..\<enviromente-name>\Scripts\activate
```

- install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

- Create .env based in .envExample

- Before running:
```
In config.py:
    Check if CHROME EXECUTABLE_PATH points to chromedriver.exe
In confest.py:
    heck if options.binary_location points to chromedriver.exe
    Check if service points to chromedriver.exe
```

- test the app:
```bash
pytest ./tests/test_login_page.py
```

- expected image:

![img](./img/test_done.PNG)

- code of example test:

```python
# validate if button exist(by xpath)

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import pytest
from tests.test_base_page import BaseTest
from ext.login_page import LoginPage

class Test_Login(BaseTest):
    
    def test_signup_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_signup_link_exist()
        assert flag


```



--------------------

### Author

Jefferson -> jefferson.almeida@global.ntt
Will -> william.yizima@global.ntt


---
## References

[chocolatey](https://chocolatey.org/install)

[venv](https://www.pythoncentral.io/how-to-install-virtualenv-python/)

[GoogleChrome Driver](https://chromedriver.chromium.org/downloads)

[Geeko Driver](https://github.com/mozilla/geckodriver/releases)

[Selenium Find Elements](https://selenium-python.readthedocs.io/locating-elements.html)

---

## Helpers

1. Pytest:

```
# run pytest in path 'apollo_tests'
pytest

# run pytest in path 'apollo_tests' and show print
pytest -s

# run pytest in path 'apollo_tests' and `most verbose`
pytest -s -vv

```
