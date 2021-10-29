FROM team STONEDLEGENDAGORA/PROUDINDIANBOT:latest

RUN git clone https://github.com/STONEDLEGENDAGORA/PROUDINDIANBOT.git ./LEGENDUSERBOT
RUN pip install --upgrade pip
RUN pip3 install -r ./PROUDINDIANBOT/requirements.txt

WORKDIR ./PROUDINDIANBOT

CMD ["python3", "-m", "userbot"]
