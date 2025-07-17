FROM nginx:latest

# Remove ALL site configs
RUN rm -f /etc/nginx/conf.d/*

# Copy our custom config
COPY nginx.conf /etc/nginx/nginx.conf
