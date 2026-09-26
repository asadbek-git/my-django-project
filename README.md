# my-django-project

Django frameworkida yaratilgan o‘zbekcha boshlang‘ich loyiha.

Python 3.10 yoki undan yangiroq versiya va `pip` kerak.

## Lokal ishga tushirish

Virtual muhitni loyiha papkasida yarating va faollashtiring:

```sh
python3 -m venv venv
source venv/bin/activate
```

Windows PowerShell uchun faollashtirish buyrug‘i:

```powershell
venv\Scripts\Activate.ps1
```

Bog‘liqliklarni o‘rnating, bazani tayyorlang va serverni ishga tushiring:

```sh
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Sayt `http://127.0.0.1:8000/` manzilida ochiladi.
`http://127.0.0.1:8000/hello/` manzili `Hello, World!` javobini qaytaradi.

Hello endpoint testini ishga tushirish:

```sh
python manage.py test hello
```

## GitHub'ga joylash

1. GitHub hisobingizga kiring va **New repository** orqali `my-django-project` nomli repository yarating. **Add a README file** opsiyasini tanlang.
2. Repository yaratilgach, uning manzilini lokal loyihaga ulang:

```sh
git remote add origin https://github.com/USERNAME/my-django-project.git
git pull origin main --allow-unrelated-histories --no-rebase
```

Remote README va lokal README to‘qnashsa, README faylida loyihaga tegishli bitta matnni qoldirib, merge'ni yakunlang:

```sh
git add README.md
git commit -m "Merge GitHub README"
git push -u origin main
```

Loyihadagi boshlang‘ich Git commiti `Initial commit`, sozlamalar uchun keyingi commit esa `Added new settings` nomi bilan yaratiladi.

Virtual muhit, `.env` fayli va lokal SQLite bazasi Git'ga kiritilmaydi. Ishlab chiqarish muhitiga joylashdan oldin `myproject/settings.py` ichidagi `SECRET_KEY` va `DEBUG` sozlamalarini xavfsiz muhit o‘zgaruvchilaridan foydalanadigan qilib o‘zgartiring.
