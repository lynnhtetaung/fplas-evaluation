import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('ElevatedButton Sample'),
        ),
        body: const Center(
          child: ElevatedButton(
            onPressed: () {
              print('Button Pressed');
            },
            child: Text(
              'Click Me',
              style: TextStyle(fontSize: 16),
            ),
          ),
        ),
      ),
    );
  }
}
