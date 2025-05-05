import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Exercise 1 - Container';

    return MaterialApp(
      title: title,
      home: Scaffold(
        body: Container(
          // Decoration for the whole Scaffold content
          decoration: BoxDecoration(
            border: Border.all(
              color: Colors.black,
              width: 10.0,
            ),
            color: Colors.white,
          ),
          child: Column(
            children: [
              AppBar(
                title: const Text(title),
                backgroundColor: Colors.blue,
                titleTextStyle: const TextStyle(
                  color: Colors.white, // AppBar title text color
                  fontWeight: FontWeight.bold, // AppBar title text weight
                  fontSize: 30, // AppBar title text size
                ),
              ),
              Expanded(
                child: Center(
                  child: Container(
                    padding: const EdgeInsets.all(16.0),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Card(
                          color: Colors.blue, // Change to blue
                          child: SizedBox(
                            width: 400, // Update width
                            height: 400, // Update height
                            child: Center(
                              child: Text(
                                'Flutter', // Updated text
                                style: const TextStyle(
                                  color: Colors.white, // Change text color to white
                                  fontSize: 50,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
