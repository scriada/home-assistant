FROM lscr.io/linuxserver/homeassistant:latest

# install pyglowmarkt for HildeBrand DCC
RUN pip install --no-cache-dir pyglowmarkt
