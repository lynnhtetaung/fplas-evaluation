import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String selectedItem = 'Apple';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Dropdown Example')),
        body: Center(
          child: DropdownButton<String>(
            value: selectedItem,
            items: const [
              DropdownMenuItem(
                value: 'Apple',
                child: Text('Apple'),
              ),
            ],
            onChanged: (String? newValue) {
              setState(() {
                selectedItem = newValue!;
              });
            },
          ),
        ),
      ),
    );
  }
}
