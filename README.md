# Please Build "watch --run" Issue

Please doesn't appear to completely kill a running process before restarting it when using `plz watch --run`.  Steps to reproduce:

1. Clone this repo
2. Run `./pleasew watch --run //src/api`
3. Visit http://localhost:8000/ to verify the flask app is serving a response
4. Change `src/api/main.py` to return something other than "hello"
5. Notice in the terminal that please knows it needs to restart, but the original python process is never killed, judging from the error output:
    ```
    OSError: [Errno 48] Address already in use
    10:34:38.169   ERROR: Command failed: Error running command plz-out/bin/src/api/api.pex: exit status 1
    ```
    The other reason I believe the original process was never killed is that if you visit http://localhost:8000/ once more, the API responds with the original text, _not_ the changed text that triggered the rebuild.
