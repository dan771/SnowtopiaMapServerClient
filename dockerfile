FROM nginx:alpine

# Get required packages for dotnet
RUN apk add bash icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib wget
RUN apk add libgdiplus --repository https://dl-3.alpinelinux.org/alpine/edge/testing/

# Install dotnet
RUN mkdir -p /usr/share/dotnet \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet
RUN wget https://dot.net/v1/dotnet-install.sh
RUN chmod +x dotnet-install.sh
RUN ./dotnet-install.sh -c 6.0 --install-dir /usr/share/dotnet
RUN ./dotnet-install.sh -c Current --runtime aspnetcore

# Install Python & Pip
RUN apk add --no-cache python3 py3-pip
RUN pip install beautifulsoup4

# Copy all files to right directories
COPY ./nginx.conf /etc/nginx/nginx.conf

# Create directories
RUN mkdir /web && mkdir /web/app && mkdir /web/public

COPY ./src/ /web/app/
COPY ./public/ /web/public/

# Set rights
RUN /bin/bash -c 'chmod +x /web/app/Process.py'

#run the script that sets up cronjob + nginx
EXPOSE 8080
COPY runtime-mod.sh /bin/
CMD /bin/runtime-mod.sh
