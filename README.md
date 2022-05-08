***APKHoarder is nolonger maintained, see [AutoDroid](https://github.com/user1342/AutoDroid).***


<p align="center">
    <img width=100% src="hoarder-logo.png">
  </a>
</p>
<p align="center"> 📱 Perform mass actions on all APKs on a device 📦</p>

<br>

# APK Hoarder
APK Hoarder is a lightweight Python program that aggregates all applications on an Android device and performs configurable tasking on them (e.g. pull, configure, push, etc).
 - Pull all APKs off a device 📱
 - Mass decompilation of APKs 📦
 - Perform bulk operations on the APKs ⚙️

APK Hoarder's main use is to download all applications installed onto a device, however, due to it's modular ```tasking``` format can perform more powerful operations - such as downloading an apk, running a tools to patch it, and then both uninstall the old apk and install the new one.

## Installation
APK Hoarder is fairly simple and so doesn't require any installation requirements, simply clone the repo and run the ```APK-Hoarder``` Python file.

```
python3 APK-Hoarder.py
```

**Currently only one device connected via ADB is supported.**

## Configuration 
APK Hoarder will perform automated tasks on all APKs on a device. The example tasking configuration provided, as seen below, will download all APKs on the device to the Python script's CWD.

```json
{
  "tasks": [
    "adb pull <applications_path>"
  ]
}
```

The following keywords can be used in the tasking config which will be switched out at runtime.
- ```<applications_path>``` - This will be replaced with the application's path on the Android device. For example ```/system/app/YouTube/YouTube.apk```.
- ```<applications_name>``` - This will be replaced with the application's name - for example ```YouTube.apk```. This can be used for accessing the file locally if ```adb pull``` was used.
- ```<iteration>``` - This will be replaced with the number of the application being analysed - e.g. ```1```. Can be used as a unique ID.
