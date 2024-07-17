
# Deployment Steps

<details>
<summary>For VPS</summary>

### First, install Python And Pip if you haven't already.

#### For Ubuntu/Debian

1. **Update the package list:**
   ```sh
   sudo apt update
   ```
2. **Install Python 3:**
   ```sh
   sudo apt install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo apt install python3-pip
   ```

#### For CentOS/RHEL

1. **Install the EPEL repository:**
   ```sh
   sudo yum install epel-release
   ```
2. **Install Python 3:**
   ```sh
   sudo yum install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo yum install python3-pip
   ```

#### For Fedora

1. **Update the package list:**
   ```sh
   sudo dnf update
   ```
2. **Install Python 3:**
   ```sh
   sudo dnf install python3
   ```
3. **Install `pip` for Python 3:**
   ```sh
   sudo dnf install python3-pip
   ```

#### For Arch Linux

1. **Update the package list:**
   ```sh
   sudo pacman -Syu
   ```
2. **Install Python and `pip`:**
   ```sh
   sudo pacman -S python python-pip
   ```

After running these commands, you should have both Python and `pip` installed on your VPS. You can verify the installations by running:

```sh
python3 --version
pip3 --version
```

### Now Create a Folder Named 'myBots' You can use any name you want.

To create a folder (directory) in Linux Vps, you need to use the `mkdir` command.

1. **Create a directory:**
   ```sh
   mkdir myBots
   ```
2. **Verify if directory is created or not:**
   ```sh
   ls
   ```

### Lets Enter To The Folder

1. **Change directory:**
   ```sh
   cd ./myBots
   ```
2. **Verify if directory is changed or not:**
   ```sh
   pwd
   ```

### Clone the Repo In The Folder `myBots` In Your VPS

1. **Clone the Repo Using this:**
   ```sh
   git clone https://github.com/Rishikesh-Sharma09/Auto-Filter-Bot   ```
2. **Verify if Repo is cloned or not:**
   ```sh
   ls
   ```

### Now Create A Virtual Environment

1. **Create A Virtual Environment:**
   ```sh
   python3 -m venv venv
   ```
2. **Verify if Virtual Environment is created or not:**
   ```sh
   ls
   ```
3. **Activate Virtual Environment:**
   ```sh
   source venv/bin/activate
   ```

### Now Enter To Our Bot Folder 'rk-filter-bot'

```sh
cd ./rk_filter_bot
```

### Edit info.py For Variables <span style="color:red ;opacity:0.5">#Optional</span>

If you want to edit any variable in your VPS then you can edit it here using:

```sh
nano ./info.py
```

Edit the Variables as per your need.

- To Save The edit use `Ctrl+O` then `Enter` and `Ctrl+X`

### Now Install All Requirements

```sh
pip3 install -r requirements.txt
```

### Now Run The Bot

```sh
python3 bot.py
```

<b style="color:skyblue">**Now Your Bot Is Ready 🔥**</b>

</details>


<details>
<summary>For Koyeb Or Render</summary>




### Deploying this bot in Render is Almost same as deploying it in Koyeb. You Just need to Follow the Steps.




- Fork the Repo And Import it in Koyeb or Render By Choosing Web Services.
- Choose python3 if any Server Asks For it.
- For Koyeb In Builder Section Choose Buildpack option.
- For Render Use This Build Command: `pip install -r requirements.txt`.
- For Koyeb You don't need to add Any Build Command.
- For run or start command, use this command: `python3 bot.py`. If you encounter a "same port error," change the port number (5001). In Koyeb, you need to enable it.
- If you are using Render then add a Variable in Environment named `PYTHON_VERSION` with value `3.10.8`.
- Add All Env Variables In Environment Variables Section.




### Now Your Bot Is Ready To Deploy🔥




</details>




<details>
<summary>For Heroku</summary>




- Create A new app in Heroku.
- Import the forked repo.
- Deploy it.
- Add all Env Variables in app settings in Heroku.
- Check Resources if the dyno is on or off. If off, then turn it on.




### Now Your Bot Is Ready In Heroku Server🔥




</details>


### If Any Problem With Deployment Don't Hesitate To Ask in Support Group.
