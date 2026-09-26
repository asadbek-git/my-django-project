# Django loyihasi

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

## GitHub'ga joylash

1. GitHub hisobingizga kiring va **New repository** orqali yangi repository yarating.
2. Repository nomini tanlang. README lokalda mavjud bo‘lgani uchun GitHub'da README bilan boshlashni tanlamang.
3. Loyiha papkasida Git'ni boshlang va birinchi commitni yarating:

```sh
git init -b main
git add .
git commit -m "Initial Django project"
```

4. GitHub ko‘rsatgan repository manzilini remote sifatida qo‘shib, yuboring:

```sh
git remote add origin https://github.com/USERNAME/REPOSITORY.git
git push -u origin main
```

Virtual muhit, `.env` fayli va lokal SQLite bazasi Git'ga kiritilmaydi. Ishlab chiqarish muhitiga joylashdan oldin `myproject/settings.py` ichidagi `SECRET_KEY` va `DEBUG` sozlamalarini xavfsiz muhit o‘zgaruvchilaridan foydalanadigan qilib o‘zgartiring.