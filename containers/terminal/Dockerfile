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
        docker.io \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pywal

# Theming
RUN bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)" \
    && sed -i '/OSH_THEME=/s/.*/OSH_THEME="cupcake"/' /root/.bashrc \
    && sed -i 's/\\W/\\w/' /root/.oh-my-bash/themes/cupcake/cupcake.theme.sh \
    && wal --theme base16-dracula && echo 'cat ~/.cache/wal/sequences' >> /root/.bashrc

CMD "/usr/bin/ttyd" "-t" "fontSize=20" "-t" "titleFixed='Terminal'" "-W" "bash" 
    