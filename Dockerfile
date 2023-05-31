FROM python:3

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./v1.py" ]
CMD ["sh", "./start.sh"]