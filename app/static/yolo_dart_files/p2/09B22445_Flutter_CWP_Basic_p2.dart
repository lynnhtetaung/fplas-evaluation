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
        	home: Scaffold(
            	appBar: AppBar(
                	title: const Text(appTitle),
                ),
                body: const Center(
                	child: Padding(
                    	padding: EdgeInsets.all(16.0),
                        child: TextField(
                            decoration: InputDecoration(
                                border: OutlineInputBorder(),
                                labelText: 'Enter name',
                            ),
                        ),
                    ),
                ),
            ),
        );
    }
}