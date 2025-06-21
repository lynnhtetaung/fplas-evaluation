import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ドロップダウンの例',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: DropdownExample(),
    );
  }
}

class DropdownExample extends StatefulWidget {
  @override
  _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample> {
  String _selectecItem = 'りんご';
  final List<String> _items = ['りんご', 'ばなな', 'みかん', 'ぶどう'];
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ドロップダウンの例'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            DropdownButton<String>(
              value: _selectedItem,
              items: _items.map((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
              onChanged: (String? newValue) {
                setState(() {
                  _selectecItem = newValue!;
                });
              },
            ),
            SizeBox(height: 20),
            Text(
              '選択された項目: $_selectedItem',
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}