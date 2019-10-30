FROM python:3

RUN git clone https://github.com/abcapo/Parcial-Tres.git
WORKDIR /Parcial-Tres

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_tateti.py"]