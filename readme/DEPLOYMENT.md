# Deployment Steps

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
cd ./rk-filter-bot
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
