"""Launch the verified RouteSafe release on Streamlit Community Cloud."""
import hashlib
import io
from pathlib import Path
import runpy
import tempfile
from urllib.request import urlopen
from zipfile import ZipFile

import streamlit as st

URL = "https://github.com/AhmedJohani/RouteSafe-System/releases/download/v1.0/RouteSafe_v1.0.zip"
DIGEST = "42e80bf94dcfda78bd452807fe20e4ee7ac48e13125245e47f880dacefc9fc62"
LIMIT = 16 * 1024 * 1024


@st.cache_resource(show_spinner=False)
def release_directory():
    with urlopen(URL, timeout=40) as response:
        data = response.read(LIMIT + 1)
    if len(data) > LIMIT or hashlib.sha256(data).hexdigest() != DIGEST:
        raise ValueError("RouteSafe release integrity check failed")
    directory = tempfile.TemporaryDirectory(prefix="routesafe-")
    with ZipFile(io.BytesIO(data)) as archive:
        archive.extractall(directory.name)
    return directory


directory = release_directory()
runpy.run_path(str(Path(directory.name) / "RouteSafe" / "app" / "dashboard.py"))
