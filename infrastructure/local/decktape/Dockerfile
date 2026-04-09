FROM astefanutti/decktape:3.4.1

COPY --chown=node:node ./create-slide-files.js /decktape

ENTRYPOINT ["node", "/decktape/create-slide-files.js"]
CMD []
