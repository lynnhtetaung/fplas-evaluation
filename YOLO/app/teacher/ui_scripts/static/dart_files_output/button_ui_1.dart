
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Button Example'),
        ),
        body: Center(
          child: ElevatedButton(
            onPressed: () {
              // Your button action here
            },
            style: ElevatedButton.styleFrom(
              primary: Colors.orange, // Set your button color here
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12), // Adjust padding for size
              elevation: 2,  // Subtle shadow for the button
              shape: const StadiumBorder(), // Standard rounded button, not too curved
            ),
            child: Text(
              'Submit',
              style: TextStyle(fontSize: 20), // Adjust font size to make it look neat
            ),
          ),
        ),
      ),
    );
  }
}
