# This is How I Setup Valet annd Cloudflare-Warp To Work Together

When I try to setup [valet linux+](https://valetlinux.plus/) and [Cloudflare-Warp](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/download-warp/#linux) I always have this problem, its either warp can't work properly or I completly can access the internet.
So, to make my life easier when setup this again here I am writing this note.

# Setup Steps:

1. Install Cloudflare-Warp, 
    - I'am not using latest version(2023.x.x)
    - I use version 2022.4.235, you can download it [here](https://web.archive.org/web/20230218043526/https://pkg.cloudflareclient.com/uploads/cloudflare_warp_2022_4_235_1_amd64_c71a3ae2e7.deb)
    - You can see list of the version [here](https://web.archive.org/web/20230218043526/https://pkg.cloudflareclient.com/packages/cloudflare-warp)
    - after download version you want run:
        ```
        sudo dpkg -i cloudflare-warp*.deb
        ```
2. Install Valet Dependencies
    ```
    sudo apt-get install curl network-manager libnss3-tools jq xsel

    sudo add-apt-repository ppa:ondrej/nginx

    sudo add-apt-repository ppa:ondrej/php

    sudo apt install -y php8.2 nginx mysql-server php-mysql php8.2-curl composer
    ```

3. Setup Mysql root password. [Read more here](https://askubuntu.com/questions/1029177/error-1698-28000-access-denied-for-user-rootlocalhost-at-ubuntu-18-04)
    ```
    sudo mysql
    ```

    ```mysql
    USE mysql;

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; 
    ```

    ```
    sudo service mysql restart
    ```

3. Install Valet. Don't use latest version first(after install you can update this)
    ```
    composer global require genesisweb/valet-linux-plus:1.5 -W

    valet install

    composer global require genesisweb/valet-linux-plus
    ```
