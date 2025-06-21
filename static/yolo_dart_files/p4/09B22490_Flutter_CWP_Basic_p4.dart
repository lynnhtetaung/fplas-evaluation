import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'チェックボックスの例',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: CheckboxExample(),
    );
  }
}

class CheckboxExample extends StatefulWidget {
  @override
  _CheckboxExampleState CreateState() => _CheckboxExampleState();
}

class _CheckboxExampleState extends State<CheckboxExample> {
  bool _isChecked = false;
  
  void _toggleCheckbox(bool? value) {
    setState(() {
      _isChecked = value ?? false;
    });
  }
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('チェックボックスの例'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              mainAxisSize: MainAxixSize.min,
              children: [
                Checkbox(
                  value: _isChecked,
                  onChanged: _toggleCheckbox,
                ),
                Text('同意する'),
              ],
            ),
            SizeBox(height: 20),
            Text(
              _isChecked ? 'チェックされています' : 'チェックされていません',
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}