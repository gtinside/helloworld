FROM python:3.8.3-buster
WORKDIR /app
COPY . /app
# install app dependencies
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTONPATH}:/app"
CMD [ "python", "read-csv.py" ]