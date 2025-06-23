import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
        return const MaterialApp(
        	debugShowCheckedModeBanner: false,
        	home: Scaffold(
            	body: Center(
                	child: SimpleCheckbox(),
                ),
            ),
        );
    }
}

class SimpleCheckbox extends StatefulWidget{
	const SimpleCheckbox({super.key});
    
    @override
    State<SimpleCheckbox> createState() => _SimpleCheckboxState();
}

class _SimpleCheckboxState extends State<SimpleCheckbox> {
	bool _isChecked = true;
    
    @override
    Widget build(BuildContext context) {
    	return Checkbox(
        	value: _isChecked,
            onChanged: (bool? value) {
            	setState(() {
                	_isChecked = value ?? false;
                });
            },
        );
    }
}