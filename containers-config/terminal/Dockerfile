FROM tsl0922/ttyd

# Install various dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y \
        python3-pip \
        vim \
        git \
        wget \
        update-motd \
        htop \
        iputils-ping \
        docker.io \
        coreutils \
        bash-completion \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pywal
# Copy our scripts
COPY ./scripts/teleport /bin/teleport
RUN chmod +x /bin/teleport

COPY ./scripts/teleport-autocomplete /etc/bash_completion.d/teleport_autocomplete
RUN chmod +x /etc/bash_completion.d/teleport_autocomplete

# Theming
RUN bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)" \
    && sed -i '/OSH_THEME=/s/.*/OSH_THEME="cupcake"/' /root/.bashrc \
    && sed -i 's/\\W/\\w/' /root/.oh-my-bash/themes/cupcake/cupcake.theme.sh \
    && wal --theme base16-dracula
COPY config/default.bashrc /root/.bashrc
CMD "/usr/bin/ttyd" "-t" "fontSize=16" "-t" "titleFixed='Terminal'" "-W" "bash" 
    
