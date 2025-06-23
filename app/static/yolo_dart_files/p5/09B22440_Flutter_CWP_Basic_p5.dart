import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'Dropdown Example',
            home: DropdownExample(),
        );
    }
}

class DropdownExample extends StatefulWidget{
	@override
    _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample>{
	String _selectedItem = 'Apple';
    final List<String> _items = ['Apple'];
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	backgroundColor: Color(0xFFFDF5F9),
            body: Center(
            	child: Container(
                	padding: EdgeInsets.symmetric(horizontal: 12),
                    decoration: BoxDecoration(
                    	border: Border.all(color: Colors.redAccent),
                        borderRadius: BorderRadius.circular(8),
                    ),
                    child: DropdownButtonHideUnderline(
                    	child: DropdownButton<String>(
                        	value: _selectedItem,
                            icon: Icon(Icons.arrow_drop_down),
                            items: _items.map((String value){
                            	return DropdownMenuItem<String>(
                                	value: value,
                                    child: Container(
                                    	color: Color(0xFFFFEEF0),
                                        padding: EdgeInsets.symmetric(horizontal: 8),
                                        child: Text(value),
                                    ),
                                );
                            }).toList(),
                            onChanged: (String? newValue){
                            	setState((){
                                	_selectedItem = newValue!;
                                });
                            },
                            dropdownColor: Color(0xFFFFEEF0),
                        ),
                    ),
                ),
            ),
        );
    }
}