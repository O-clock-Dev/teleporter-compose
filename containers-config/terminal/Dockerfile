FROM tsl0922/ttyd

# Install various dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y \
        python3-pip \
        vim \
        git \
        wget \
        curl \
        gnupg2 \
        update-motd \
        htop \
        iputils-ping \
        docker.io \
        coreutils \
        bash-completion \
        mysql-client \
        ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Installation of postgresql repo
RUN install -d /usr/share/postgresql-common/pgdg && \
    curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc && \
    sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' && \

# Installation of node repo
RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    echo "deb https://deb.nodesource.com/node_20.x bullseye main" | tee /etc/apt/sources.list.d/nodesource.list

RUN apt-get update && apt-get install -y nodejs postgresql-client-16 && npm install -g n && \
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/* && apt-get clean

RUN pip3 install --no-cache-dir pywal

# Copy our scripts
COPY ./scripts/teleport /bin/teleport
RUN chmod +x /bin/teleport

COPY ./scripts/teleport-autocomplete /etc/bash_completion.d/teleport_autocomplete
RUN chmod +x /etc/bash_completion.d/teleport_autocomplete

# Theming
RUN bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)" 

# Entrypoint
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
