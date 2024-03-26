from rembg import remove
import base64

from typing import Annotated
from fastapi import FastAPI, UploadFile, Request, Body
from fastapi.templating import Jinja2Templates

import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def health(request: Request):
    return templates.TemplateResponse('dynamic.html', { "request": request })

@app.post("/remove")
def remove_bg(request: Request, file: UploadFile, mask_only: Annotated[bool, Body()]):
    data = file.file.read()

    output_array = remove(data, only_mask=mask_only)

    output_img = base64.b64encode(output_array).decode('utf-8')

    file.file.close()

    encoded_image = base64.b64encode(data).decode('utf-8')
    
    return templates.TemplateResponse(
        'dynamic.html',
        {
            "request" : request,
            "image" : encoded_image,
            "output_img" : output_img
        }
    )

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
