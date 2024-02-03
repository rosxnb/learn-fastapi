##############################################################################
#
# `File()` or `UploadFile()` function can be used state that operations requires user to send file.
#
# Use File() for small files with bytes as data type.
#
# Use UploadFile() for large files like photo, video, etc
#   because UploadFile() exposes python's `SpooledTemporaryFile()` object
#   which can be used to pass file to other libraries.
#
# >> pip install python-mulipart
#
##############################################################################


from typing import Annotated
from fastapi import FastAPI, File, UploadFile


server = FastAPI()


@server.post("/file/")
async def create_files(file: Annotated[bytes, File()]):
    return { "file_size": len(file) }


@server.post("/uploadfile")
async def create_upload_file(
    file: Annotated[
        UploadFile,
        File(
            description = "File() can also be used for Annotation to provide metadata"
        )
    ]
):
    return { "filename": file.filename }




######################################################################################
# Multiple Files upload

from fastapi.responses import HTMLResponse

@server.post("/files/")
async def create_files(
    files: Annotated[
        list[bytes],
        File(
            description="Multiple files as bytes"
        )
    ],
):
    return { "file_sizes": [len(file) for file in files] }


@server.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], 
        File(
            description="Multiple files as UploadFile"
        )
    ],
):
    return { "filenames": [file.filename for file in files] }


@server.get("/")
async def main():
    content = """
        <body>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit">
            </form>
        </body>
    """
    return HTMLResponse(content=content)
