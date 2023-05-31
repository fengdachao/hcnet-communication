FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "./test_main.py", "-dbackend Agg" ]
# CMD ["sh", "./start.sh"]