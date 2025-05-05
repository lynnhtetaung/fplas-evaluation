import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Exercise 3 - Vertical ListView';

    return MaterialApp(
      title: title,
      home: Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black, // Border color
            width: 10.0, // Border width for the entire Scaffold
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text(title),
            backgroundColor: Colors.blue,
            titleTextStyle: const TextStyle(
              color: Colors.white, // AppBar title text color
              fontWeight: FontWeight.bold, // AppBar title text weight
              fontSize: 30, // AppBar title text size
            ),
          ),
          body: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 20.0),  // Add horizontal padding
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,  // Center the containers vertically
              children: <Widget>[
                Container(
                  height: 150,
                  color: Colors.red,
                  alignment: Alignment.center,
                ),
                Container(
                  height: 150,
                  color: Colors.white,
                  alignment: Alignment.center,
                ),
                Container(
                  height: 150,
                  color: Colors.blue,
                  alignment: Alignment.center,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
