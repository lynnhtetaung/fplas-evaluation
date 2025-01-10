
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Icon Example'),
        ),
        body: Center(
          child: Icon(
            Icons.settings,
            size: 100.0,
            color: Colors.blue,  // Change the color as per your preference
          ),
        ),
      ),
    );
  }
}
