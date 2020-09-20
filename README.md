# APK Hoarder
APK Hoarder is a lightweight Python program that aggregates all applicatios on an Android device and performs configurable tasking on them (e.g. pull, configure, push, etc).

APK Hoarder's main use is to download all applications installed onto a device, however, due to it's modular ```tasking``` format can perform more powerful operations - such as downloading an apk, running a tools to patch it, and then both uninstall the old apk and install the new one.

## Installation
APK Hoarder is fairly simple and so doesn't require any installation requirements, simply clone the repo and run the ```APK-Hoarder``` Python file.

```
python3 APK-Hoarder.py
```

**Currently only one device connected via ADB is supported.**

## Configuration 
APK Hoarder will perform automated tasks on all APKs on a device. The example tasking configuration provided, as seen below, will download al APKs on the device to the Python scripts CWD.

```json
{
  "tasks": [
    "adb pull <applications_path>"
  ]
}
```

The following keywords can be used in the tasking config which will be switched out at runtime.
- ```<applications_path>``` - This will be replaced with the application's path on the Android device. For example ```/system/app/YouTube/YouTube.apk```.
- ```<applications_name>``` - This will be replaced with the application's name - for example ` ``YouTube.apk```. This can be used for accessing the file locally if ```adb pull``` was used.
