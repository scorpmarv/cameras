# cameras

1. pip is required

```
$ sudo apt-get install python3-pip
```

2. Now that pip is installed we need to install virtualenv

```
$ sudo pip install virtualenv
```

3. Create a virtualenv

```
$ virtualenv -p python3.6 env
```

4. Activate the virtualenv

```
$ source env/bin/activate
```

5. Install dependencies

```
$ pip install roman
```

6. Run the code: it will create a new file dict.json

```
$ python main.py
```
