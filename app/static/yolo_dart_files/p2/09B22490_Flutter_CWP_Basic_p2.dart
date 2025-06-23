import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'テキストフィールドの例',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TextFieldExample(),
    );
  }
}

class TextFieldExample extends statefulWidget {
  @override
  _TextFieldExampleState createState() => _TextFieldExampleState();
}

class _TextFieldExampleState extends State<TextFieldExample> {
  String _inputText = "";
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('テキストフィールドの例'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              decoration: InputDecoration(
                labelText: 'テキストを入力してください',
                border: OutlineInputBorder(),
              ),
              onChanged: (text) {
                setState(() {
                  _inputText = text;
                });
              },
            ),
            SizedBox(height: 20),
            Text(
              '入力されたテキスト: $_inputText',
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}