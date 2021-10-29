FROM teamlegend/Legendbot:latest

RUN git clone https://github.com/StonedLegend/PROUD-INDIAN-BOT.git ./PROUDINDIANBOT
RUN pip install --upgrade pip
RUN pip3 install -r ./PROUDINDIANBOT/requirements.txt

WORKDIR ./PROUDINDIANBOT

CMD ["python3", "-m", "userbot"]
