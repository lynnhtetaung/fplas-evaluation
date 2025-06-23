import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: DropdownCenterPage(),
    );
  }
}

class _DropdownCenterPageState extends State<DropdownCenterPage> {
  String _salectedValue = '選択しろ';
  
  final List<String> _items = ['選択しろ','りんご','バナナ','みかん'];
  
  @override
  Widget build(uildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('好きな果物')),
      body: Center(
        child: DropdownButton<String>(
          value: _selectedValue,
          items: _items.map((String value){})
            return DropdownMenuItem<String>(
              value: value,
              child: Text(value),
            );
          }).toList(),
          onChanged: (String? newValue) {
            setState(() {
              _selectedValue = newValue!;
            });
          },
        ),
      ),
    );
  }
}

















