import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ElevatedButton Demo',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Button Example'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              // ボタンが押されたときの処理
              print('Button clicked');
            },
            child: const Text('Click me'),
          ),
        ),
      ),
    );
  }
}