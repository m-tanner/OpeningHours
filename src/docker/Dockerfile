FROM python:3.7-alpine

RUN echo Copying the oh service into a service directory.
COPY . /OpeningHoursService
WORKDIR /OpeningHoursService

RUN echo Adding the new folder to the Python path so that Flask works.
ENV PYTHONPATH /OpeningHoursService

RUN echo Installing APK and Python packages listed in setup.py
RUN apk update
RUN \
 apk add --no-cache --virtual .build-deps libffi-dev gcc musl-dev && \
 python3 -m pip install . --no-cache-dir && \
 apk --purge del .build-deps

RUN echo Exposing the port where Waitress will listen.
EXPOSE 8080

RUN echo Starting python and starting the Flask service...
CMD ["run_svc"]
