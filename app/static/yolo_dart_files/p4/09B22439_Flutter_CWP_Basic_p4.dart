import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: MyCheckbox(), 
        );
    }
}

class MyCheckbox extends StatefulWidget {
	@override
    _MyCheckboxState createState() => _MyCheckboxState();
}

class _MyCheckboxState extends State<MyCheckbox> {
	bool isChecked = true;
    
    @override
    Widget build(BuildContext context) {
    	return Scaffold(
        	body: Center(
            	child: Row(
                	mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                    	Checkbox(
                        	value: isChecked,
                        	onChanged: (bool? value) {
                        		setState(() {
                            		isChecked = value ?? false;
                            	});
                        	},
                            activeColor: Colors.blue,
                    	),
                    ],
                ),
            ),
        );
    }
}