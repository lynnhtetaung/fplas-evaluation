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
                titleTextStyle: TextStyle(
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
                          color: Colors.blue,
                          child: SizedBox(
                            width: 400,
                            height: 400,
                            child: Center(
                              child: Text(
                                'Flutter',
                                style: TextStyle(
                                  color: Colors.white,
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



