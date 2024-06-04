FROM tsl0922/ttyd

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_DISTRIB=focal

# Install curl gnupg
RUN apt update \
    && apt install -y curl gnupg2 wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install repositories (pgsql, node, yarn, gh)
RUN install -d /usr/share/postgresql-common/pgdg \
    && curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc \
    && sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt ${DEBIAN_DISTRIB}-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

RUN curl -fsSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
    && echo "deb https://deb.nodesource.com/node_20.x ${DEBIAN_DISTRIB} main" | tee /etc/apt/sources.list.d/nodesource.list

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN mkdir -p -m 755 /etc/apt/keyrings \
    && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
    && chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install dependencies
RUN apt update \
    && apt install -y \
        python3-pip \
        vim \
        git \
        curl \
        update-motd \
        htop \
        iputils-ping \
        docker.io \
        coreutils \
        bash-completion \
        mariadb-client \
        ca-certificates \
        nodejs \
        postgresql-client-16 \
        yarn \
        gh \
    && npm install -g n \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

# pywal
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
