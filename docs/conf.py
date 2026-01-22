import os

# force argparse to wrap usage more tightly for autoprogram
os.environ["COLUMNS"] = "65"

project = "cm-proxy"
copyright = "2025-2026, CauseMatch Israel Ltd <foss@causematch.com>"
author = "Aryeh Leib Taurog, Evgeni Zabus, Paritosh Gupta, and Geva Or"
version = "0.2.3"
release = version

master_doc = "index"

needs_sphinx = "9.0"
extensions = ["alabaster", "sphinxcontrib.autoprogram"]

html_theme = "alabaster"

html_theme_options = {
    "github_user": "causematch",
    "github_repo": "cm-proxy",
    "github_button": True,
    "github_type": "star",
    "description": "A quick, cheap, secure, and straightforward serverless localhost proxy",
    "fixed_sidebar": True,
    "extra_nav_links": {
        "github": "https://github.com/causematch/cm-proxy",
        "pypi": "https://pypi.python.org/pypi/cm-proxy",
    },
}
