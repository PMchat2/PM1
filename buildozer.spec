[app]
title = 隐私通讯程式
package.name = privatebinchat
package.domain = org.privatebin
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pem
version = 0.1

# ---- 必须列全依赖项 ----
requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.1,requests,urllib3,chardet,idna,certifi,pycryptodome

# ---- Android 权限 ----
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# ---- Android 编译参数（关键修复：固定版本，避免自动选新版出错）----
android.api = 33
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
