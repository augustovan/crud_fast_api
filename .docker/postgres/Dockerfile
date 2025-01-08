FROM postgres:13

RUN chmod +x /usr/local/bin/*

# Configurar o PATH para incluir os binários do PostgreSQL
ENV PATH="/usr/lib/postgresql/16/bin:${PATH}"

# Definir o diretório de trabalho
WORKDIR /usr/local/bin