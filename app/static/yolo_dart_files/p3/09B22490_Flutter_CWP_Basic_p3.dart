import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});
  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: Center(
          child: ElevatedButton(
            child: Text('Click me!'),
            onPressed: () {
              print('Thank you!');
            }
          ),
        ),
      ),
    );
  }
}
