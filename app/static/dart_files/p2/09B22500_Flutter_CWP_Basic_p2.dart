import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
        ),
        body: Center(
          child: Container(
            width: 300,
            height: 100,
            padding: EdgeInsets.all(12),
            decoration: BoxDecoration(
              border: Border.all(
                color: Colors.green,
                width: 3,
              ),
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Enter name',
                  style: TextStyle(
                    color: Colors.green,
                    fontSize: 18,
                  ),
                ),
                SizeBox(
                  width: 150,
                  child: TextField(
                    decoration: InputDecoration(
                      isDense: true,                   
                      contentPadding: EdgeInsets.symmetric(vertical: 8, horizontal: 8),
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}