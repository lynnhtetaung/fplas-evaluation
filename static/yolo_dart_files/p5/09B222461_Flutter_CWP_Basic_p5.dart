import 'package:flutter/material.dart';

void main(){
	runApp(const MyApp());
}

class MyApp extends StatelessWidget{
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context){
    	return MaterialApp(
        	debugShowCheckedModeBanner: false,
        	home: DropdownExample(),
        );
    }
}

class DropdownExample extends StatefulWidget{
	@override
    _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample>{
	String? _selectedValue = 'apple';
    
    final List<String> _items = ['apple', 'orange', 'banana'];
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	appBar: AppBar(title: const Text('Example')),
            body: Center(
            	child: DropdownButton<String>(
                	value: _selectedValue,
                    onChanged: (String? newValue){
                    	setState((){
                        	_selectedValue = newValue;
                        });
                    },
                    items: _items.map((String item){
                    	return DropdownMenuItem<String>(
                        	value: item,
                            child: Text(item),
                        );
                    }).toList(),
                ),
            ),
        );
    }
}