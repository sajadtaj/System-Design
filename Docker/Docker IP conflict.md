<div dir="rtl">
## 🧩 ** بررسی رنج IPهای conflict شده با docker یا bridge دیگر**

```bash
ip a
```

و بررسی پیکربندی:

```bash
cat /etc/docker/daemon.json
```

---

## 🧩 **. بررسی نام DNS/Hostname و رفع خطای resolve**

### بررسی hostname:

```bash
hostname
```

### بررسی و اصلاح فایل hosts:

```bash
cat /etc/hosts
```

اصلاح:

```bash
127.0.0.1 your-hostname
```

---

## 🧪 **مطالعه موردی (Case Study):**

### خطا:

سرویس داکر روی پورت `5050` اجرا شده ولی از شبکه شرکت دیده نمی‌شود.

### تحلیل:

* `ip a`: مشاهده شده `docker0` از رنج `172.17.0.0/16` استفاده می‌کند.
* این رنج با LAN شرکت Amazon تداخل دارد → کانفلیکت

### راه‌حل:

باید رنج IP انرا تغییر دهیم تا دیگر مانند مشابه سرویس داخلی آمازون نباشد
تغییر `/etc/docker/daemon.json`:

ابتدا از پروایدر سازمان رنجIp مطمعن را بپرسید

>> مثلا: `x.x.x.1/24`


```bash
sudo nano /etc/docker/daemon.json
```

انرا به ادرس زیر تغییر دهید:

```json
{
  "bip": "x.x.x.1/24"
}
```

و سپس:

```bash
sudo systemctl restart docker
```

