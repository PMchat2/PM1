[app]
title = 隐私通讯程式
package.name = privatebinchat
package.domain = org.privatebin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pem
version = 0.1

# ---- 必须列全依赖项，openssl 解决 SSL 证书问题 ----
requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.1,requests,urllib3,chardet,idna,certifi,openssl,pycryptodome

# ---- Android 权限（补齐所有需要的权限）----
android.permissions = INTERNET, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE, WAKE_LOCK, POST_NOTIFICATIONS

# ---- Android 编译参数（适配 Android 16 / API 35）----
android.api = 35
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.archs = arm64-v8a
android.accept_sdk_license = True
android.allow_backup = True

# ---- 日志 ----
log_level = 2

# ---- 屏幕方向 ----
orientation = portrait
