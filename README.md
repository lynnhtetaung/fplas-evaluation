# exercise1

A new Flutter project.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.

# Correct answer title can show in the center for macOS.
# Correct answer title can show in the left side for window and linux. ( Container Example )

# If you want to modify default chrome dart file directly
root@1081e2c33273:/app# vim /usr/local/flutter/packages/flutter_tools/lib/src/web/chrome.dart 


# Docker-compose explanation

Interactive Shell:

stdin_open: true and tty: true allow you to attach a terminal to the flutter-app container so you can manually run commands (e.g., flutter build web).
Shared Volume: The shared-data volume is still used to store the built files, which are shared between flutter-app and nginx-app.


# To upload Docker images to the DockerHub.

docker login

docker tag <local_image_id> <dockerhub_username>/<repository_name>:<tag>
Eg. 
docker tag flutter-app 24091997/fplas-backend-2024:v1
docker tag nginx-app 24091997/fplas-nginx-2024:v1
docker tag nplas-app 24091997/fplas-frontend-2024:v1


docker push <dockerhub_username>/<repository_name>:<tag>
Eg.
docker push 24091997/fplas-backend-2024:v1
docker push 24091997/fplas-nginx-2024:v1
docker push 24091997/fplas-frontend-2024:v1


## need to install tesseract
sudo apt update
sudo apt install tesseract-ocr
tesseract --version


# reference docker file and index.html
https://github.com/edwardinubuntu/flutter-web-dockerfile


# To check image is exist or not 
docker cp plas-flutter-app-1:/app/static/output/studentID_Flutter_CMP_Basic_problemNumber.png .

docker cp plas-flutter-app-1:/app/static/output/4D23414212_Flutter_CMP_Basic_p3.png .

