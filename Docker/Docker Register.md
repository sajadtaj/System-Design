### **۱. توضیح پارامترهای فایل `/etc/resolv.conf`**  
فایل `resolv.conf` برای تنظیم **سیستم نام دامنه (DNS)** استفاده می‌شود. این فایل شامل سرورهای DNS است که برای تبدیل نام دامنه (مثل `google.com`) به آدرس IP مورد استفاده قرار می‌گیرند.

#### **پارامترهای مهم در `resolv.conf`**  
| پارامتر | توضیح |
|---------|-------|
| `nameserver` | آدرس IP یک سرور DNS که برای ترجمه نام دامنه استفاده می‌شود. چندین `nameserver` می‌توان اضافه کرد. |
| `search` | دامنه‌هایی که هنگام جستجوی نام‌ها به‌طور خودکار اضافه می‌شوند. |
| `options` | شامل گزینه‌های اضافی مانند `timeout` و `attempts` برای کنترل درخواست‌های DNS. |

✅ **نمونه تنظیمات پیشنهادی برای `/etc/resolv.conf`**:  
```bash
nameserver 10.202.10.10
nameserver 10.202.10.11
nameserver 1.1.1.1
options timeout:2 attempts:3
```

---

### **۲. توضیح پارامترهای فایل `/etc/docker/daemon.json`**  
فایل `daemon.json` برای پیکربندی داکر استفاده می‌شود. این فایل شامل تنظیمات مرتبط با رجیستری‌ها، لاگ‌ها، شبکه و سایر موارد است.

#### **پارامترهای مهم در `daemon.json`**  
| پارامتر | توضیح |
|---------|-------|
| `registry-mirrors` | آدرس‌های جایگزین برای کش کردن و بهبود سرعت دریافت ایمیج‌ها از **Docker Hub**. |
| `insecure-registries` | مشخص کردن رجیستری‌هایی که از HTTPS استفاده نمی‌کنند و داکر بدون خطای امنیتی از آن‌ها ایمیج دریافت کند. |
| `debug` | فعال یا غیرفعال کردن لاگ‌های خطایابی داکر. مقدار `true` باعث نمایش لاگ‌های دقیق‌تر می‌شود. |
| `storage-driver` | مشخص کردن درایور ذخیره‌سازی که داکر برای مدیریت ایمیج‌ها و کانتینرها استفاده می‌کند. |

✅ **نمونه تنظیمات پیشنهادی برای `daemon.json`**:  
```json
{
  "registry-mirrors": ["https://docker.iranserver.com"],
  "insecure-registries": ["https://docker.iranserver.com"],
  "debug": true
}
```

---

## **۳. نحوه اعمال تغییرات در فایل‌ها**
### **الف) تنظیم فایل `/etc/resolv.conf` برای استفاده از DNSهای داخلی ایران**  
1. ویرایش فایل `resolv.conf` با ویرایشگر `nano`:
   ```bash
   sudo nano /etc/resolv.conf
   ```
2. اضافه کردن سرورهای DNS مورد نظر:
   ```
   nameserver 10.202.10.10
   nameserver 10.202.10.11
   nameserver 1.1.1.1
   ```
3. ذخیره فایل با `CTRL + X`، سپس `Y` و `Enter`.

✅ **نکته:** این تغییرات ممکن است بعد از ری‌استارت سرور به حالت اولیه بازگردند. برای ثابت نگه داشتن این تنظیمات، از دستور زیر استفاده کنید:
   ```bash
   sudo chattr +i /etc/resolv.conf
   ```
   برای برداشتن قفل:
   ```bash
   sudo chattr -i /etc/resolv.conf
   ```

---

### **ب) تنظیم فایل `/etc/docker/daemon.json` برای استفاده از میرورهای داکر**
1. ویرایش فایل `daemon.json`:
   ```bash
   sudo nano /etc/docker/daemon.json
   ```
2. افزودن یا تغییر مقادیر زیر:
   ```json
   {
     "registry-mirrors": ["https://docker.manageit.ir"],
     "insecure-registries": ["https://docker.manageit.ir"]
   }
   ```
3. ذخیره فایل (`CTRL + X` → `Y` → `Enter`).
4. **ری‌استارت داکر برای اعمال تغییرات:**
   ```bash
   sudo systemctl restart docker
   ```
5. **تست عملکرد:**  
   ```bash
   docker info | grep "Registry Mirrors"
   ```

✅ **نکته:** اگر بعد از تغییر `daemon.json` داکر اجرا نشد، خطاهای آن را بررسی کنید:
   ```bash
   sudo systemctl status docker
   sudo journalctl -u docker --no-pager | tail -n 50
   ```

---
### جدول ۱: **DNSهای پیشنهادی برای `/etc/resolv.conf`**
| نام ارائه‌دهنده | DNS 1 | DNS 2 |
|---------------|------------|------------|
| **رادار** | `10.202.10.10` | `10.202.10.11` |
| **الکترو** | `78.157.42.100` | `78.157.42.101` |
| **شلتر** | `94.103.125.157` | `94.103.125.158` |
| **بشکن** | `181.41.194.177` | `181.41.194.186` |
| **پیشگامان** | `5.202.100.100` | `5.202.100.101` |
| **Level3** | `209.244.0.3` | `209.244.0.4` |
| **کلودفلر** | `1.1.1.1` | `1.0.0.1` |
| **شکن** | `178.22.122.100` | `185.51.200.2` |
| **403** | `10.202.10.202` | `10.202.10.102` |

---

### جدول ۲: **تنظیمات `daemon.json` (میرورها و رجیستری‌های داکر)**
| نام ارائه‌دهنده | `insecure-registries` | `registry-mirrors` |
|---------------|------------------------|----------------------|
| **ایران‌سرور** | `https://docker.iranserver.com` | `https://docker.iranserver.com` |
| **آروان‌کلود** | `https://docker.arvancloud.ir` | `https://docker.arvancloud.ir` |
| **ManageIT** | `https://docker.manageit.ir` | `https://docker.manageit.ir` |
| **Runflare** | `https://mirror-docker.runflare.com` | `https://mirror-docker.runflare.com` |
| **GCR** | `https://mirror.gcr.io/registry` | `https://mirror.gcr.io/registry` |
| **HaioCloud** | `https://docker.haiocloud.com` | `https://docker.haiocloud.com` |
| **USTC** | `https://docker.mirrors.ustc.edu.cn` | `https://docker.mirrors.ustc.edu.cn` |
| **TWUN** | `https://helm.twun.io` | `https://helm.twun.io` |

