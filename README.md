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

root@1081e2c33273:/app# vim /usr/local/flutter/packages/flutter_tools/lib/src/web/chrome.dart 


Docker-compose explanation

Interactive Shell:

stdin_open: true and tty: true allow you to attach a terminal to the flutter-app container so you can manually run commands (e.g., flutter build web).
Shared Volume: The shared-data volume is still used to store the built files, which are shared between flutter-app and nginx-app.