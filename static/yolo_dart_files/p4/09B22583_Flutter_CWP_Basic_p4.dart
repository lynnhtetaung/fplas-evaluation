import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'Checkbox Demo',
            home: Scaffold(
            	appBar: AppBar(
                	title: const Text('Example (例)'),
                ),
                backgroundColor: const Color(0xFFF8F0FF),
                body: const Center(
                	child: MyCheckboxWidget(),
                ),
            ),
        );
    }
}

class MyCheckboxWidget extends StatefulWidget {
	const MyCheckboxWidget({super.key});
    
    @overide
    State<MyCheckboxWidget> creareState() => _MyCheckboxWidgetState();    
}

class _MyCheckboxWidgetState extends State<MyCheckboxWidget> {
	bool _isChecked = true;
    
    @override
    Widget build(BuildContext context) {
    	return Checkbox(
        	value: _isChecked,
            onChanged: (bool? newValue) {
            	setState(() {
                	_isChecked = newValue!;
                });
            },
        );
    }
}