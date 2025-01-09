
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Flutter Dropdown Example'),
        ),
        body: Center(
          child: DropdownButton<String>(
            items: [
              DropdownMenuItem(value: 'Option 2', child: Text('Option 2')),
                  DropdownMenuItem(value: 'Option 4', child: Text('Option 4')),
                  DropdownMenuItem(value: 'Option 3', child: Text('Option 3'))
            ],
            onChanged: (value) {},
            hint: const Text('Select one'),
            // Increase the size of the dropdown
            iconSize: 30.0, // Increase the size of the dropdown icon
            style: TextStyle(fontSize: 20.0), // Increase the font size of the text
            dropdownColor: Colors.white, // Optional: Adjust dropdown background color
            isExpanded: true, // Make the dropdown button fill available space
            padding: EdgeInsets.symmetric(horizontal: 20.0), // Add padding for larger size
          ),
        ),
      ),
    );
  }
}
