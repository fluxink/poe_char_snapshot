
FROM python:3.10

# Install LuaJIT
RUN apt-get update && apt-get install -y luajit

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./backend/ .

COPY PathOfBuilding/runtime/lua /usr/local/share/lua/5.1/