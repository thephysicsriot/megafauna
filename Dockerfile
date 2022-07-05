FROM python:3.7.3
COPY app/requirements.txt /tmp/
RUN python -m pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
COPY . /tmp/
WORKDIR /tmp/
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000