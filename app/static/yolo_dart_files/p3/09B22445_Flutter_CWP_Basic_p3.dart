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
                	child: ElevatedButton(
                    	onPressed: _handleButtonPress,
                        child: Text('Click me'),
                    ),	
                ),
            ),
        );    
    }
    
    static void _handleButtonPress(){
    	debugPrint('Button was pressed.');
    }
}