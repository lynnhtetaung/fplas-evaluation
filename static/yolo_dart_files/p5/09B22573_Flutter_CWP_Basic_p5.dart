import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        title: 'dropdown',
        home: Scaffold(
        	appBar:AppBar(
            	title: const Text('dropDown'),
            ),
            body: const Center(
            	child: SimpleDropdown(),
            ),
        ),
        );
    }
}

class SimpleDropdown extends StatefulWidget {
	const SimpleDropdown({super.key});
    
    @override
    State<SimpleDropdown> createState() => _SimpleDropdownState();
}

class _SimpleDropdownState extends State<SimpleDropdown> {
	final List<String> _items = ['A','B','C'];
    String? _selectedValue;
    
    @override
    Widget build(BuildContext context) {
     return Padding(
     	padding: const EdgeInsets.all(20.0),
        child: DropdownButton<String>(
        	hint: const Text('Choose'),
            value: _selectedValue,
            onChanged: (String? newValue) {
            	setState((){
                	_selectedValue = newValue;
                });
            },
            items: _items.map<DropdownMenuItem<String>>((String itemValue) {
            	return DropdownMenuItem<String>(
                	value: itemValue,
                    child: Text(itemValue),
                );
            }).toList(),
        ),
     );
    }

}
