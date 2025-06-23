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
	bool isChecked = true;
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
            	body: Center(
                	child: Checkbox(
                    	value: isChecked,
                        onChanged: (bool? value) {
                        	setState(() {
                            	isChecked = value ?? false;
                            });
                        },
                    ),
                ),
            ),
        );
    }
}