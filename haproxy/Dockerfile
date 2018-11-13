# vim:set ft=dockerfile:
FROM alpine:3.8

ENV HAPROXY_MAJOR 1.9
ENV HAPROXY_VERSION 1.9-dev6
ENV HAPROXY_SHA256 90ce4eab016359151ac3ce35e5eb418f89d9a36f43db19c7e8fdc089707ed4d2

# use edge version of alpine to use openssl 1.1.1 / TLS 1.3
#RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" > /etc/apk/repositories \
#	&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories \
#	&& apk upgrade --update-cache --available \
#	&& apk update
# The above breaks certbot ! 

# see https://sources.debian.net/src/haproxy/jessie/debian/rules/ for some helpful navigation of the possible "make" arguments
RUN set -x \
	\
	&& apk add --no-cache --virtual .build-deps \
		ca-certificates \
		gcc \
		libc-dev \
		linux-headers \
		lua5.3-dev \
		make \
		openssl \
		openssl-dev \
		pcre-dev \
		readline-dev \
		tar \
		zlib-dev \
		wget \
	\

# update certs
	&& update-ca-certificates \

# install HAProxy
	&& wget -O haproxy.tar.gz "https://www.haproxy.org/download/${HAPROXY_MAJOR}/src/devel/haproxy-${HAPROXY_VERSION}.tar.gz" \
	&& echo "$HAPROXY_SHA256 *haproxy.tar.gz" | sha256sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	\
	&& makeOpts=' \
		TARGET=linux2628 \
		USE_LUA=1 LUA_INC=/usr/include/lua5.3 LUA_LIB=/usr/lib/lua5.3 \
		USE_OPENSSL=1 \
		USE_PCRE=1 PCREDIR= \
		USE_ZLIB=1 \
	' \
	&& make -C /usr/src/haproxy -j "$(getconf _NPROCESSORS_ONLN)" all $makeOpts \
	&& make -C /usr/src/haproxy install-bin $makeOpts \
	\
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy \
	\
	&& runDeps="$( \
		scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \
			| tr ',' '\n' \
			| sort -u \
			| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
	)" \
	&& apk add --virtual .haproxy-rundeps $runDeps \
	&& apk del .build-deps

# https://www.haproxy.org/download/1.8/doc/management.txt
# "4. Stopping and restarting HAProxy"
# "when the SIGTERM signal is sent to the haproxy process, it immediately quits and all established connections are closed"
# "graceful stop is triggered when the SIGUSR1 signal is sent to the haproxy process"
STOPSIGNAL SIGUSR1

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]

# For auto generating let's encrypt cert with a AWS Route 53 hosted zone. See Readme.md
RUN apk add --no-cache --virtual .pynacl_deps python3 build-base python3-dev libffi-dev openssl openssl-dev \
  && rm -rf /var/cache/apk/* \
  && pip3 install --upgrade pip \
  && pip3 install certbot certbot-dns-route53
COPY aws-config /root/.aws/config
RUN certbot certonly -n --agree-tos --email schietzsch@googlemail.com --dns-route53 -d ff2k.net --staging
RUN cat /etc/letsencrypt/live/ff2k.net/fullchain.pem /etc/letsencrypt/live/ff2k.net/privkey.pem > /usr/local/etc/ff2k_full.pem
