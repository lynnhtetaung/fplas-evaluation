import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'ElevatedButton Demo',
            home: Scaffold(
            	appBar: AppBar(
                	title: const Text('Example (例)'),
                );
                body: const Center(
                	child: ElevatedButton(
                    	onPressrd: null, 
                        child: Text('Click me'),
                    ),
                ),
                backgroundColor: Color(0xFFF8F0FF),
            ),
        );
    }
}