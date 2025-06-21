import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	const String appTitle = 'Flutter layout demo';
        return MaterialApp(
        	title: appTitle,
            home: Scaffold(
            	body: const Center(
                	child: Text('This is sample text'),
                ),
            ),
        );
    }
    
}