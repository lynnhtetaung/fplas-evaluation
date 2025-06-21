import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	home: DropdownSample(),
        );
    }
}

class DropdownSample extends StatefulWidget{
	@override
    _DropdownSampleState createState() => _DropdownSampleState();
}

class _DropdownSampleState extends State<DropdownSample>{
	String _selectedValue = 'Apple';
    
    final List<String> _items = ['Apple','Orange'];
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	appBar: AppBar(
            	title: Text('Dropdown Sample'),
            ),
            body: Center(
            	child: DropdownButton<String>(
                	value: _selectedValue,
                    onChanged: (String? newValue){
                    	setState((){
                        	_selectedValue = newValue!;
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