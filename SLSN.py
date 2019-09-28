import pickle
import numpy as np
from astropy.table import Table
from astropy.io import ascii
import os
import requests
import json
from datetime import datetime
from astropy.table import Table
from astropy.time import Time
from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
from astropy import constants as const
import matplotlib.pyplot as plt
import matplotlib
import getpass
import warnings
import pandas
import time
import subprocess
import logging
import webbrowser
import glob
from datetime import *

username = "AishwaryaD"
password = "bBrA@7592"

targets = ["ZTF18abszecm","ZTF18acenqto","ZTF18acxgqxq","ZTF19aarphwc","ZTF19aawsqsc","ZTF19aavouyw",
"ZTF19aaqrime","ZTF19abaeyqw","ZTF18aaisyyp","ZTF18aajqcue","ZTF18aapgrxo","ZTF18aavrmcg","ZTF18aazgrfl",
"ZTF18abjwagv","ZTF18ablwafp","ZTF18abmasep","ZTF18abrzcbp","ZTF18abshezu","ZTF18abvgjyl","ZTF18acapyww",
"ZTF18achdidy","ZTF18acqyvag","ZTF18acslpji","ZTF18acyxnyw","ZTF19aacxrab","ZTF19aajwogx","ZTF19aaknqmp",
"ZTF19aamhhiz","ZTF19aanesgt","ZTF19aantokv","ZTF19aaohuwc","ZTF19aapaeye","ZTF19aaruixj","ZTF19aasdvfr",
"ZTF19aauiref","ZTF19aayclnm","ZTF19abdlzyq","ZTF19abfvnns"]

for t in targets:
