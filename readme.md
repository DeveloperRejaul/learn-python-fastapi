## Setup Project
### Doc : https://fastapi.tiangolo.com/virtual-environments/

1. Create virtual environment

```bash
python -m venv .venv 
or 
python3 -m venv .venv 
```

2. Activate the Virtual Environment
```bash
source .venv/bin/activate
```

3. Check the Virtual Environment is Active
```bash
which python
or 
which python3
# shoud retun path like this : /home/user/code/awesome-project/.venv/bin/python
```

4. Upgrade pip (optional)
```bash
python -m pip install --upgrade pip
or
python3 -m pip install --upgrade pip
```

5. Add .gitignore (optional)
```bash
echo "*" > .venv/.gitignore
```

6. Install Packages
```bash
pip install "fastapi[standard]"
```
7. Run Your Program
```bash
python main.py
or
python3 main.py
```

8. Deactivate the Virtual Environment
```bash
deactivate
```

9. Run the live server:
```bash
fastapi dev main.py
```

10. Start custom port
```bash
pip install "uvicorn[standard]"
uvicorn main:app --host 0.0.0.0 --port 4000
```


11. Build the Docker Image
```bash
docker build -t myimage .
```

12. Start the Docker Container
```bash
docker run -d --name mycontainer -p 80:80 myimage
```

13. Pipenv PipFile setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pipenv
pipenv install

# install package
pipenv install requests

# And to start a shell inside the environment:
pipenv shell
```