# auto_attendance_moodle

This is a program for you who too lazy for open elearning/moodle to set attendance by self, so I made this for you.

I'm using Python3, selenium for build this bot.

I have tested and it worked, hehe

**FYI**, this script is not running automatically if the day of attendance is coming, if you want to run automatically you can use `cronjob`, you can search on google how to use it.

Clone this repository

```bash
git clone https://github.com/kdimas12/auto_attendence_moodle.git
```

then move to directory

```bash
cd auto_attendence_moodle
```

install dependency

```bash
pip3 install requirements.txt
```

and you can just run the program

```bash
python3 automate.py
```

or

```bash
python3 automate.py <password>
```

**but before you run this script, you have to configure the program first!**

1. You have to add account to file `akun.json`, with format
   ```bash
    {
      "nama": "this is your name",
      "username": "your username",
      "password": "and this is your password"
    }
   ```
   you can add multiple account, so the program will run until all account have set attendance, for example:
   ```bash
    {
      "nama": "first acc",
      "username": "first username",
      "password": "first password"
    },
    {
      "nama": "second acc",
      "username": "second username",
      "password": "second password"
    }
   ```
2. And then you have to add link attendance courses to `matakuliah.json` with format:

   ```bash
    {
      "weekday": 1,
      "nama": "Name of course",
      "link": "this is a link for your attendance"
    },
    {
      "weekday": 3,
      "nama": "second name of course",
      "link": "this is a link for your attendance"
    }
   ```

   `"weekday"` is a day of a week it start from 0 is monday, so you can set the day which course attendance is set.

3. Then edit file `automate.py` in `chooseCourses()` function to the day courses attendance is set.

   ```bash
   def chooseCourses():
   date = datetime.now()
   url = ""

   if date.weekday() == 1:
       # prak. pemrograman visual hari selasa
       url = openCoursesJson(1)
   elif date.weekday() == 3:
       # pemrograman visual hari kamis
       url = openCoursesJson(3)
   return url
   ```

   for example I have course Prak. Pemrograman Visual it set attendance for Tuesday, so I write `if date.weekday() == 1` and `openCoursesJson(1)`

   \*weekday is start with 0 = monday, so 0, 1, 2, 3, 4, 5, 6 = monday, tuesday, wednesday, thursday, friday, saturday, sunday

After all file configured you can now run the script

```bash
python3 automate.py
```

or if the attendance have password you can run

```bash
python3 automate.py <password>
```

Okeyy, that's it I hope you can use it well. I hope you can contribute for this project to add more feature or fix a bug :)

Thanks
