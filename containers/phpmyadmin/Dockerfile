FROM phpmyadmin:5.2.1  

RUN mv /var/www/html /var/www/phpmyadmin && mkdir -p /var/www/html && mv /var/www/phpmyadmin /var/www/html/phpmyadmin
COPY ./blueberry-1.1.0 /var/www/html/phpmyadmin/themes/