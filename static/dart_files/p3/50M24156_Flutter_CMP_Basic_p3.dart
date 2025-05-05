import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Exercise 3 - Horizontal ListView';

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
             titleTextStyle: TextStyle(
              color: Colors.white, // AppBar title text color
              fontWeight: FontWeight.bold, // AppBar title text weight
              fontSize: 30, // AppBar title text size
            ),
          ),
          body: Center(
            child: Padding(
              padding: const EdgeInsets.all(20.0),  // Padding to keep the ListView away from the border
              child: Container(
                height: 300,  // Height of the container (adjust as necessary)
                child: ListView(
                  scrollDirection: Axis.horizontal, // Set to horizontal scrolling
                  children: <Widget>[
                    Container(
                      width: 400,
                      color: Colors.blue,
                      alignment: Alignment.center,
                    ),
                    const SizedBox(width: 20),  // Spacing between containers
                    Container(
                      width: 400,
                      color: Colors.white,
                      alignment: Alignment.center,
                    ),
                    const SizedBox(width: 20),  // Spacing between containers
                    Container(
                      width: 450,
                      color: Colors.red,
                      alignment: Alignment.center,
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}


