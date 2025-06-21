import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	const String appTitle = 'Flutter dropdown demo';
        return MaterialApp(
        	home: Scaffold(
            	appBar: AppBar(
                	title: const Text(appTitle),
                ),
                body: const Center(
                	child: DropdownExample(),
                ),
            ),
        );
    }
}

class DropdownExample extends StatefulWidget {
	const DropdownExample({super.key});
    
    @override
    State<DropdownExample> createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample> {
	final List<String> items = ['Apple','Orange','peach'];
    String? selectedItem;
    
    @override
    Widget build(BuildContext context) {
    	return DropdownButton<String>(
        	hint: const Text('Choose fruits.'),
            value: selectedItem,
            items: items.map((String value) {
            	return DropdownMenuItem<String>(
                	value: value,
                    child: Text(value),
                );
            }).toList(),
            onChanged: (String? newValue) {
            	setState(() {
                	selectedItem = newValue;
                });
            },
        );
    }
}