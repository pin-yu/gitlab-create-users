# Easily Create Users of Gitlab

## Usage

### Install required packages
```bash
pip install -r requirements.txt
```

### Create gitlab config
```bash
cp python-gitlab.cfg.example python-gitlab.cfg
```

After that copy your private token and paste it to the cfg file.

You probably need to grant `api` and `sudo` permission for creating users.

### Run the script to create users
```bash
python ./create_users/main.py --xls [MEMBER XLS]
```



