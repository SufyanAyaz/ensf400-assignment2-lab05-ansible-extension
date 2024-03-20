FROM alpine:latest


# Install Nginx
RUN apk update && apk add nginx


COPY nginx.cfg /etc/nginx/nginx.cfg


EXPOSE 80


CMD ["nginx", "-g", "daemon off;"]