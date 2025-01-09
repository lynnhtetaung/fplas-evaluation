
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Checkbox Example'),
        ),
        body: Center(
          child: Checkbox(
            value: true,  // You can set this to false if you want the checkbox to be unchecked
            onChanged: (bool? newValue) { 
              // Handle checkbox state change
            },
            activeColor: Colors.blue,  // Color when checked
            checkColor: Colors.white,  // Color of the check mark
            materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
            // Adjust the size of the checkbox
          ),
        ),
      ),
    );
  }
}
