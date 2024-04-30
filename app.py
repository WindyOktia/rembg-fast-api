import base64

from rembg import remove, new_session

from typing import Annotated
from fastapi import FastAPI, UploadFile, Request, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse, Response

import uvicorn

import os

os.environ['U2NET_HOME'] = './models/'

model_names = [
    'u2net',
    'u2net_human_seg',
    'u2net_cloth_seg',
    'isnet-general-use',
]

sessions = {
    'u2net': new_session(model_name=model_names[0]),
}

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def health(request: Request):
    return templates.TemplateResponse('dynamic.html', { "request": request })


@app.post("/remove")
async def remove_bg(
    request: Request,
    file: Annotated[UploadFile, File()],
    mask_only: Annotated[str, Form()] = 'off',
    name_of_model: Annotated[str, Form()] = 'u2net'
) -> HTMLResponse:
    try:
        if name_of_model not in sessions.keys():
            sessions[name_of_model] = new_session(model_name=name_of_model)
        
        current_session = sessions[name_of_model]

        only_mask = mask_only == 'on'
        data = await file.file.read()

        output_array = remove(data, only_mask=only_mask, session=current_session)

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
    except:
        return RedirectResponse("/", status_code=303)


@app.post("/remove_bg")
async def remove_bg(
    request: Request,
    file: UploadFile,
    mask_only: str = 'off',
    name_of_model: str = 'u2net'
):
    try:
        if name_of_model not in sessions.keys():
            sessions[name_of_model] = new_session(model_name=name_of_model)
        
        current_session = sessions[name_of_model]

        only_mask = mask_only == 'on'
        data = file.file.read()

        output_array = remove(data, only_mask=only_mask, session=current_session)

        file.file.close()
        
        return Response(content=output_array, media_type="image/png")
    except Exception as error:
        return f"Oopss!!!! {error}"

@app.get("/remove")
def remove_bg_redirect():
    return RedirectResponse('/')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7860)
