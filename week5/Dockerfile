FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict_flask.py", "model1.bin", "dv.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--host=0.0.0.0", "--port=9696", "predict_flask:app"]
