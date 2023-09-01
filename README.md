in Docker:

[x] GET endpoint, which give back count of api calls to its endpoint

[x] connected postgres db in separate Container

[x] via docker-compose

[ ] served from Azure

[ ] another independent app with an endpoint, which just responses with a string

[ ] application which combines these calls into a single application, docker containers managed by Kubernetes?

[ ] terraform?





# endpunkt soll die db automatisch initialisieren.. erst local ausprobieren
# TODO HIER WEITER: ah mist, gar nicht sicher, ob das jetzt rein in docker läuft, hatte local app laufen. 
#  nochmal fresh testen


#  $ docker run -itd -e POSTGRES_USER=stefan -e POSTGRES_PASSWORD=123 -p 5432:5432 -v C:/work/projects/docker-volumes/postgres:/var/lib/postgresql/data --name stefanpostgres postgres
#  im container terminal: PGPASSWORD=123 psql -U stefan
#  dann mal mit dem fastapi cookiecutter system vergleichen


