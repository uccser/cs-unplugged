FROM traefik:v2.4.8
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json
COPY ./infrastructure/local/traefik/traefik.yml /etc/traefik
