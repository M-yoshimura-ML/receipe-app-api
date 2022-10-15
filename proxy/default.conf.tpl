server {
  listen ${LISTEN=PORT};

  location /static {
    alias /vol/static;
  }

  location / {
    uwsgi_pass           ${APP_HOST}:${APP_PORT};
    inclode              /ect/nginx/uwsgi_params;
    client_max_body_size 10M;
  }
}
