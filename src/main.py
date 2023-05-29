import requests
from bs4 import BeautifulSoup
from typing import Union
from fastapi import FastAPI
import re
import uvicorn

app = FastAPI(title="Direct Download",
              version="0.0.1",
              terms_of_service=
              "Use It Only For Personal Project Else I Need To Delete The Api",
              contact={
                "name": "JTGTGAMES",
                "url": "https://github.com/JTGTGAMES",
              },
              docs_url='/')

uvicorn.run(app, host='0.0.0.0')
