FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN mkdir ~/.u2net/

COPY ./models/*.onnx ~/.u2net/

RUN mkdir src
RUN mkdir app

WORKDIR /src/app

COPY ./requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "fast_app.py" ]